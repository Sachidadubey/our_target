"""Report generator for Government Job Research System.
Formats intelligence databases into markdown tables, alerts, and executive briefs.
"""

from typing import List, Dict, Any


class ReportGenerator:
    @staticmethod
    def format_status_badge(status: str) -> str:
        mapping = {
            "OPEN_NOW": "🟢 APPLY NOW",
            "OPENING_SOON": "🟡 APPLICATION OPENING SOON",
            "UPCOMING": "🔵 UPCOMING — PREPARE NOW",
            "CLOSED": "🔴 CLOSED",
            "EXAM_PENDING": "📝 EXAM STAGE",
            "RESULT_PENDING": "⏳ RESULT STAGE"
        }
        return mapping.get(status, f"⚪ {status}")

    @staticmethod
    def generate_master_markdown_table(jobs: List[Dict[str, Any]]) -> str:
        headers = [
            "Organization", "Recruitment", "Post", "CSE Eligible?", "Why eligible?",
            "Degree requirement", "Branch requirement", "Experience", "Age limit",
            "General age relaxation", "EWS eligibility", "Vacancies", "Salary",
            "Application Opens", "Application Closes", "Current Status", "Exam Date",
            "Selection Process", "Exam Pattern", "Syllabus", "Previous Cutoff",
            "Official Notification", "Official Apply Link", "Source", "Last Verified"
        ]

        lines = ["| " + " | ".join(headers) + " |"]
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

        for j in jobs:
            status_badge = ReportGenerator.format_status_badge(j.get("status", ""))
            row = [
                j.get("organization", "").replace("|", "-"),
                j.get("recruitment_name", "").replace("|", "-"),
                j.get("post_name", "").replace("|", "-"),
                j.get("cse_eligible", "YES"),
                j.get("eligibility_reason", "").replace("|", "-")[:80] + "...",
                j.get("degree_requirement", "").replace("|", "-"),
                j.get("branch_requirement", "").replace("|", "-"),
                j.get("experience_requirement", "None (Fresher)"),
                f"{j.get('age_min', 18)}–{j.get('age_max', 30)} yrs",
                "As per Govt Rules",
                j.get("ews_applicable", "YES"),
                str(j.get("vacancies", 0)),
                j.get("salary", "").replace("|", "-"),
                j.get("application_start", "N/A"),
                j.get("application_end", "N/A"),
                status_badge,
                j.get("exam_date", "TBD").replace("|", "-"),
                j.get("selection_process", "Written + Interview").replace("|", "-")[:70] + "...",
                j.get("exam_pattern", "").replace("|", "-")[:60] + "...",
                j.get("syllabus", "").replace("|", "-")[:60] + "...",
                j.get("cutoff_previous_year", "N/A").replace("|", "-")[:50] + "...",
                f"[Notification]({j.get('official_notification_url', '#')})",
                f"[Apply Portal]({j.get('official_application_url', '#')})",
                j.get("source_url", "").replace("|", "-"),
                j.get("last_verified", "01/10/2026")
            ]
            lines.append("| " + " | ".join(row) + " |")

        return "\n".join(lines)
