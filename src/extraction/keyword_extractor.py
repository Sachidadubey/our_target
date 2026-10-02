"""Keyword and text pattern extraction utilities for government notifications."""

import re
from typing import Dict, Any, Optional


class RecruitmentKeywordExtractor:
    @staticmethod
    def extract_pay_scale(text: str) -> Optional[str]:
        # Match Level 6, Level 7, Level 10, Pay Band, etc.
        m = re.search(r'(Level\s*[-–]?\s*\d{1,2}|Pay\s*Matrix\s*Level\s*\d{1,2}|Rs\.?\s*[\d,]+\s*[-–]\s*[\d,]+|PB-?\s*\d)', text, re.IGNORECASE)
        return m.group(0) if m else None

    @staticmethod
    def extract_age_bracket(text: str) -> tuple[int, int]:
        # Match age like 18-30, 20 to 27 years, etc.
        m = re.search(r'(\d{2})\s*(?:to|-|–)\s*(\d{2})\s*(?:years|yrs)?', text, re.IGNORECASE)
        if m:
            return int(m.group(1)), int(m.group(2))
        return 18, 30

    @staticmethod
    def clean_text(text: str) -> str:
        return re.sub(r'\s+', ' ', text).strip()
