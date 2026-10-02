"""Database models and persistence manager for Government Job Research System.
Uses SQLite for robust, lightweight, zero-dependency persistence.
"""

import sqlite3
import hashlib
import json
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "jobs.db")


@dataclass
class JobRecord:
    id: Optional[int] = None
    organization: str = ""
    department: str = ""
    recruitment_name: str = ""
    post_name: str = ""
    category: str = "technical"  # technical / non_technical
    cse_eligible: str = "YES"    # YES / NO / UNCERTAIN
    eligibility_reason: str = ""
    degree_requirement: str = ""
    branch_requirement: str = ""
    experience_requirement: str = "None (Fresher Eligible)"
    age_min: int = 18
    age_max: int = 30
    ews_applicable: str = "YES"
    vacancies: int = 0
    salary: str = ""
    pay_level: str = ""
    application_start: str = ""  # YYYY-MM-DD
    application_end: str = ""    # YYYY-MM-DD
    exam_date: str = ""
    notification_date: str = ""
    status: str = "OPEN_NOW"     # OPEN_NOW, OPENING_SOON, UPCOMING, CLOSED, EXAM_PENDING, RESULT_PENDING
    selection_process: str = ""
    exam_pattern: str = ""
    syllabus: str = ""
    cutoff_previous_year: str = ""
    official_notification_url: str = ""
    official_application_url: str = ""
    source_url: str = ""
    last_verified: str = ""
    content_hash: str = ""

    def generate_hash(self) -> str:
        unique_string = f"{self.organization}|{self.recruitment_name}|{self.post_name}|{self.application_end}|{self.vacancies}"
        return hashlib.sha256(unique_string.encode("utf-8")).hexdigest()


class DatabaseManager:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.init_db()

    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                organization TEXT NOT NULL,
                department TEXT,
                recruitment_name TEXT NOT NULL,
                post_name TEXT NOT NULL,
                category TEXT,
                cse_eligible TEXT DEFAULT 'YES',
                eligibility_reason TEXT,
                degree_requirement TEXT,
                branch_requirement TEXT,
                experience_requirement TEXT,
                age_min INTEGER,
                age_max INTEGER,
                ews_applicable TEXT DEFAULT 'YES',
                vacancies INTEGER,
                salary TEXT,
                pay_level TEXT,
                application_start TEXT,
                application_end TEXT,
                exam_date TEXT,
                notification_date TEXT,
                status TEXT NOT NULL,
                selection_process TEXT,
                exam_pattern TEXT,
                syllabus TEXT,
                cutoff_previous_year TEXT,
                official_notification_url TEXT,
                official_application_url TEXT,
                source_url TEXT,
                last_verified TEXT,
                content_hash TEXT UNIQUE
            );
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS change_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id INTEGER,
                field_name TEXT,
                old_value TEXT,
                new_value TEXT,
                changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(job_id) REFERENCES jobs(id)
            );
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS site_snapshots (
                url TEXT PRIMARY KEY,
                last_checked TEXT,
                content_hash TEXT,
                status_code INTEGER,
                notes TEXT
            );
            """)
            conn.commit()

    def upsert_job(self, record: JobRecord) -> Dict[str, Any]:
        """Insert or update a job record, returning change diff if modified."""
        if not record.content_hash:
            record.content_hash = record.generate_hash()

        with self.get_connection() as conn:
            cursor = conn.cursor()
            # Check by organization + recruitment_name + post_name
            cursor.execute(
                "SELECT * FROM jobs WHERE organization = ? AND recruitment_name = ? AND post_name = ?",
                (record.organization, record.recruitment_name, record.post_name)
            )
            existing = cursor.fetchone()

            if existing is None:
                # Insert fresh record
                cursor.execute("""
                INSERT INTO jobs (
                    organization, department, recruitment_name, post_name, category,
                    cse_eligible, eligibility_reason, degree_requirement, branch_requirement,
                    experience_requirement, age_min, age_max, ews_applicable, vacancies,
                    salary, pay_level, application_start, application_end, exam_date,
                    notification_date, status, selection_process, exam_pattern, syllabus,
                    cutoff_previous_year, official_notification_url, official_application_url,
                    source_url, last_verified, content_hash
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
                """, (
                    record.organization, record.department, record.recruitment_name, record.post_name,
                    record.category, record.cse_eligible, record.eligibility_reason, record.degree_requirement,
                    record.branch_requirement, record.experience_requirement, record.age_min, record.age_max,
                    record.ews_applicable, record.vacancies, record.salary, record.pay_level,
                    record.application_start, record.application_end, record.exam_date,
                    record.notification_date, record.status, record.selection_process,
                    record.exam_pattern, record.syllabus, record.cutoff_previous_year,
                    record.official_notification_url, record.official_application_url,
                    record.source_url, record.last_verified, record.content_hash
                ))
                conn.commit()
                return {"action": "INSERTED", "id": cursor.lastrowid}
            else:
                # Compare fields and log changes
                existing_dict = dict(existing)
                job_id = existing_dict["id"]
                changes = {}
                fields_to_check = [
                    "status", "application_end", "vacancies", "exam_date",
                    "salary", "official_application_url"
                ]

                record_dict = asdict(record)
                for f in fields_to_check:
                    old_val = str(existing_dict.get(f) or "")
                    new_val = str(record_dict.get(f) or "")
                    if old_val != new_val:
                        changes[f] = {"old": old_val, "new": new_val}
                        cursor.execute(
                            "INSERT INTO change_logs (job_id, field_name, old_value, new_value) VALUES (?, ?, ?, ?)",
                            (job_id, f, old_val, new_val)
                        )

                # Update current record
                cursor.execute("""
                UPDATE jobs SET
                    department = ?, category = ?, cse_eligible = ?, eligibility_reason = ?,
                    degree_requirement = ?, branch_requirement = ?, experience_requirement = ?,
                    age_min = ?, age_max = ?, ews_applicable = ?, vacancies = ?, salary = ?,
                    pay_level = ?, application_start = ?, application_end = ?, exam_date = ?,
                    notification_date = ?, status = ?, selection_process = ?, exam_pattern = ?,
                    syllabus = ?, cutoff_previous_year = ?, official_notification_url = ?,
                    official_application_url = ?, source_url = ?, last_verified = ?,
                    content_hash = ?
                WHERE id = ?
                """, (
                    record.department, record.category, record.cse_eligible, record.eligibility_reason,
                    record.degree_requirement, record.branch_requirement, record.experience_requirement,
                    record.age_min, record.age_max, record.ews_applicable, record.vacancies,
                    record.salary, record.pay_level, record.application_start, record.application_end,
                    record.exam_date, record.notification_date, record.status, record.selection_process,
                    record.exam_pattern, record.syllabus, record.cutoff_previous_year,
                    record.official_notification_url, record.official_application_url,
                    record.source_url, record.last_verified, record.content_hash, job_id
                ))
                conn.commit()
                return {"action": "UPDATED" if changes else "UNCHANGED", "id": job_id, "changes": changes}

    def get_all_jobs(self, status: Optional[str] = None, cse_only: bool = False) -> List[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM jobs WHERE 1=1"
            params = []
            if status:
                query += " AND status = ?"
                params.append(status)
            if cse_only:
                query += " AND cse_eligible = 'YES'"
            query += " ORDER BY CASE status WHEN 'OPEN_NOW' THEN 1 WHEN 'OPENING_SOON' THEN 2 WHEN 'UPCOMING' THEN 3 ELSE 4 END, application_end ASC"

            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [dict(r) for r in rows]

    def get_jobs_by_category(self, category_keyword: str) -> List[Dict[str, Any]]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM jobs WHERE category LIKE ? OR organization LIKE ? OR recruitment_name LIKE ?",
                (f"%{category_keyword}%", f"%{category_keyword}%", f"%{category_keyword}%")
            )
            return [dict(r) for r in cursor.fetchall()]
