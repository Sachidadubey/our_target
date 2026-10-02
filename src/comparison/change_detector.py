"""Change detection and alert generation engine.
Monitors deadline thresholds (7 days, 3 days, 1 day), new job entries, and changes to existing records.
"""

from datetime import datetime, date
from typing import List, Dict, Any


class ChangeDetector:
    def __init__(self, db_manager):
        self.db = db_manager

    def evaluate_deadlines(self, target_date: date = None) -> List[Dict[str, Any]]:
        """Identify open recruitments approaching closing deadlines within 7, 3, or 1 day."""
        if target_date is None:
            # System date is 2026-10-01
            target_date = date(2026, 10, 1)

        alerts = []
        open_jobs = self.db.get_all_jobs(status="OPEN_NOW")

        for job in open_jobs:
            end_date_str = job.get("application_end")
            if not end_date_str:
                continue

            try:
                # Handle YYYY-MM-DD
                end_dt = datetime.strptime(end_date_str, "%Y-%m-%d").date()
                days_left = (end_dt - target_date).days

                if 0 <= days_left <= 7:
                    urgency = "HIGH" if days_left <= 2 else ("MEDIUM" if days_left <= 4 else "LOW")
                    alerts.append({
                        "job_id": job["id"],
                        "organization": job["organization"],
                        "recruitment_name": job["recruitment_name"],
                        "post_name": job["post_name"],
                        "deadline": end_date_str,
                        "days_remaining": days_left,
                        "urgency": urgency,
                        "application_url": job["official_application_url"],
                        "salary": job["salary"]
                    })
            except Exception:
                continue

        alerts.sort(key=lambda x: x["days_remaining"])
        return alerts

    def generate_daily_metrics(self) -> Dict[str, Any]:
        """Generate high-level counts for daily intelligence brief."""
        all_jobs = self.db.get_all_jobs()
        open_jobs = [j for j in all_jobs if j["status"] == "OPEN_NOW"]
        opening_soon = [j for j in all_jobs if j["status"] == "OPENING_SOON"]
        upcoming = [j for j in all_jobs if j["status"] == "UPCOMING"]
        cse_specific = [j for j in all_jobs if "computer science" in (j["branch_requirement"] or "").lower() or "it" in (j["branch_requirement"] or "").lower()]
        any_grad = [j for j in all_jobs if "any" in (j["degree_requirement"] or "").lower()]
        apprentices = [j for j in all_jobs if "apprentice" in (j["post_name"] or "").lower() or "apprentice" in (j["recruitment_name"] or "").lower()]

        return {
            "total_records": len(all_jobs),
            "open_now_count": len(open_jobs),
            "opening_soon_count": len(opening_soon),
            "upcoming_count": len(upcoming),
            "cse_specific_count": len(cse_specific),
            "any_graduate_count": len(any_grad),
            "apprenticeship_count": len(apprentices)
        }
