"""PDF extraction tool for official government job notification circulars.
Extracts qualifications, branch eligibility, dates, and vacancies from downloaded PDFs.
"""

import os
import re
from typing import Dict, Any, List, Optional
from pypdf import PdfReader


class NotificationPDFParser:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.text = ""
        self._load_text()

    def _load_text(self):
        if not os.path.exists(self.pdf_path):
            return
        try:
            reader = PdfReader(self.pdf_path)
            pages_text = []
            # Extract first 20 pages max for performance (most notifications are within this)
            for page in reader.pages[:20]:
                extracted = page.extract_text()
                if extracted:
                    pages_text.append(extracted)
            self.text = "\n".join(pages_text)
        except Exception as e:
            self.text = ""

    def search_keywords(self, keywords: List[str]) -> List[str]:
        """Find paragraphs or sentences mentioning specified keywords."""
        if not self.text:
            return []
        matches = []
        sentences = re.split(r'[\n\.\;]', self.text)
        for s in sentences:
            s_clean = s.strip()
            if any(re.search(r'\b' + re.escape(kw) + r'\b', s_clean, re.IGNORECASE) for kw in keywords):
                if len(s_clean) > 20 and s_clean not in matches:
                    matches.append(s_clean)
        return matches[:10]

    def extract_metadata(self) -> Dict[str, Any]:
        """Extract advertisement number, closing dates, vacancies, and qualifications."""
        if not self.text:
            return {}

        meta = {}

        # Advertisement Number Pattern
        advt_match = re.search(r'(Advt\.?\s*No\.?|Notification\s*No\.?|CEN\s*No\.?|EN\s*No\.?)\s*[:\-]?\s*([A-Za-z0-9\/\-_]+)', self.text, re.IGNORECASE)
        if advt_match:
            meta["advertisement_no"] = f"{advt_match.group(1)} {advt_match.group(2)}"

        # Date Patterns (DD/MM/YYYY, DD-MM-YYYY, or Month DD, YYYY)
        date_pattern = r'(\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{4}|\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[\s,]+\d{4})'
        last_date_match = re.search(r'(?:last\s*date|closing\s*date|receipt\s*of\s*application)[^.\n]*?' + date_pattern, self.text, re.IGNORECASE)
        if last_date_match:
            meta["closing_date_snippet"] = last_date_match.group(0)

        # Total Vacancies
        vac_match = re.search(r'(?:total\s*vacanc(?:ies|y)|vacancies\s*[:\-]?)\s*(\d{1,5})', self.text, re.IGNORECASE)
        if vac_match:
            meta["vacancies"] = int(vac_match.group(1))

        # Check for Computer Science / IT branch mention
        cs_mentions = self.search_keywords(["Computer Science", "Information Technology", "CSE", "B.Tech", "B.E."])
        meta["cs_qualification_snippets"] = cs_mentions

        return meta
