"""Base scraper interface for government recruitment portals."""

from abc import ABC, abstractmethod
from typing import List
from ..database.models import JobRecord
from ..browser.playwright_manager import BrowserManager
from ..eligibility.cse_checker import CSEEligibilityChecker, CandidateProfile


class BaseScraper(ABC):
    def __init__(self, browser_mgr: BrowserManager = None):
        self.browser_mgr = browser_mgr or BrowserManager()
        self.checker = CSEEligibilityChecker(CandidateProfile())

    @abstractmethod
    def scrape_or_load(self) -> List[JobRecord]:
        """Fetch and return verified job records for this sector/portal."""
        pass
