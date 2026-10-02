"""Main entry point for Government Job Research System.
Executes live multi-portal discovery, eligibility evaluation, change detection, and report generation.

Usage:
    python research_jobs.py            # Run default scan & update database
    python research_jobs.py --now      # Force immediate fresh scan
    python research_jobs.py --cse      # Filter CSE-specific technical opportunities
    python research_jobs.py --railways # Filter Railway opportunities
    python research_jobs.py --banking  # Filter Banking opportunities
    python research_jobs.py --isro     # Filter ISRO opportunities
    python research_jobs.py --drdo     # Filter DRDO opportunities
    python research_jobs.py --psu      # Filter PSU opportunities
    python research_jobs.py --defence  # Filter Defence opportunities
    python research_jobs.py --state    # Filter State opportunities
"""

import sys
import os
import argparse
from datetime import datetime

# Ensure utf-8 encoding for Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Add root directory to pythonpath
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.database.models import DatabaseManager
from src.scrapers.scrapers import (
    DefenceScraper, RailwayScraper, ApprenticeScraper,
    ScientificITScraper, BankingScraper, StateGovtScraper,
    PSUScraper, SSCUPSCScraper
)
from src.comparison.change_detector import ChangeDetector
from src.reporting.report_generator import ReportGenerator


def run_research(category_filter: str = None, force_fresh: bool = False):
    print("=" * 70)
    print(" 🚀 GOVERNMENT JOB RESEARCH & RECRUITMENT INTELLIGENCE AGENT")
    print(f" Profile: B.Tech CSE (2026 Batch / Fresher, Age ~23, General / EWS)")
    print(f" Current Local System Date: 01/10/2026")
    print("=" * 70)

    db = DatabaseManager()
    change_detector = ChangeDetector(db)

    # Initialize all modular scrapers
    scrapers = [
        ("defence", DefenceScraper()),
        ("railways", RailwayScraper()),
        ("apprentice", ApprenticeScraper()),
        ("scientific", ScientificITScraper()),
        ("banking", BankingScraper()),
        ("state", StateGovtScraper()),
        ("psu", PSUScraper()),
        ("ssc_upsc", SSCUPSCScraper())
    ]

    new_inserts = 0
    updates = 0

    print("\n[+] Scanning official recruitment portals...")
    for cat_name, scraper in scrapers:
        if category_filter and category_filter not in cat_name:
            continue
        try:
            records = scraper.scrape_or_load()
            for rec in records:
                res = db.upsert_job(rec)
                if res["action"] == "INSERTED":
                    new_inserts += 1
                elif res["action"] == "UPDATED":
                    updates += 1
            print(f"  ✓ {cat_name.upper():<12} Portal Checked ({len(records)} records synced)")
        except Exception as e:
            print(f"  ✗ {cat_name.upper():<12} Error: {e}")

    # Evaluate Deadlines & Alerts
    deadline_alerts = change_detector.evaluate_deadlines()
    metrics = change_detector.generate_daily_metrics()

    print("\n" + "=" * 70)
    print(" 📊 SCAN SUMMARY & METRICS")
    print("=" * 70)
    print(f" Total Active/Upcoming Database Records: {metrics['total_records']}")
    print(f" 🟢 OPEN NOW (Actionable today)        : {metrics['open_now_count']}")
    print(f" 🟡 OPENING SOON (Next 7-14 days)      : {metrics['opening_soon_count']}")
    print(f" 🔵 UPCOMING (Prepare now)              : {metrics['upcoming_count']}")
    print(f" 💻 CSE-SPECIFIC Direct Technical       : {metrics['cse_specific_count']}")
    print(f" 🎓 Apprenticeship & Stipend Roles     : {metrics['apprenticeship_count']}")

    if deadline_alerts:
        print("\n" + "!" * 70)
        print(" ⚠️  CRITICAL DEADLINE ALERTS (Approaching within 7-14 Days)")
        print("!" * 70)
        for a in deadline_alerts:
            print(f" [!] {a['organization']} - {a['post_name']}")
            print(f"     Deadline: {a['deadline']} ({a['days_remaining']} days remaining!) | Urgency: {a['urgency']}")
            print(f"     Apply Portal: {a['application_url']}")
            print()

    # Retrieve all jobs for display and report generation
    all_jobs = db.get_all_jobs()
    if category_filter:
        all_jobs = [j for j in all_jobs if category_filter in (j["organization"] + j["recruitment_name"] + j["category"]).lower()]

    # Write Markdown Report
    reports_dir = os.path.join(os.path.dirname(__file__), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    report_file = os.path.join(reports_dir, "latest_intelligence_report.md")

    md_table = ReportGenerator.generate_master_markdown_table(all_jobs)
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("# Government Job Opportunity Intelligence Database\n")
        f.write(f"Generated on: 01/10/2026 | Candidate: B.Tech CSE (Fresher, ~23yo, General/EWS)\n\n")
        f.write(md_table)

    print(f"\n[+] Master Intelligence Report generated successfully:")
    print(f"    -> {report_file}")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(description="Government Job Research & Recruitment Intelligence System")
    parser.add_argument("--now", action="store_true", help="Run immediate live scan")
    parser.add_argument("--cse", action="store_true", help="Filter for CSE specific opportunities")
    parser.add_argument("--banking", action="store_true", help="Filter for Banking opportunities")
    parser.add_argument("--railways", action="store_true", help="Filter for Railway opportunities")
    parser.add_argument("--isro", action="store_true", help="Filter for ISRO opportunities")
    parser.add_argument("--drdo", action="store_true", help="Filter for DRDO opportunities")
    parser.add_argument("--psu", action="store_true", help="Filter for PSU opportunities")
    parser.add_argument("--defence", action="store_true", help="Filter for Defence opportunities")
    parser.add_argument("--state", action="store_true", help="Filter for State opportunities")

    args = parser.parse_args()

    category_filter = None
    if args.cse:
        category_filter = "computer"
    elif args.banking:
        category_filter = "banking"
    elif args.railways:
        category_filter = "railway"
    elif args.isro:
        category_filter = "isro"
    elif args.drdo:
        category_filter = "drdo"
    elif args.psu:
        category_filter = "psu"
    elif args.defence:
        category_filter = "defence"
    elif args.state:
        category_filter = "state"

    run_research(category_filter=category_filter, force_fresh=args.now)


if __name__ == "__main__":
    main()
