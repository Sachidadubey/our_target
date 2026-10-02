"""Browser and HTTP request manager for scraping official government recruitment portals.
Supports headless browser inspection via Playwright with graceful HTTP session fallback.
"""

import logging
import requests
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive"
}


class BrowserManager:
    def __init__(self, headless: bool = True, timeout_sec: int = 15):
        self.headless = headless
        self.timeout_sec = timeout_sec
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)

    def fetch_url_http(self, url: str) -> Dict[str, Any]:
        """Fetch URL using robust HTTP requests with retry and error handling."""
        try:
            response = self.session.get(url, timeout=self.timeout_sec, verify=True)
            return {
                "success": response.status_code == 200,
                "status_code": response.status_code,
                "content": response.text,
                "url": response.url,
                "error": None
            }
        except Exception as e:
            return {
                "success": False,
                "status_code": None,
                "content": "",
                "url": url,
                "error": str(e)
            }

    async def fetch_url_playwright(self, url: str) -> Dict[str, Any]:
        """Fetch URL using Playwright Chromium for JavaScript-heavy government portals."""
        try:
            from playwright.async_api import async_playwright
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=self.headless)
                context = await browser.new_context(user_agent=DEFAULT_HEADERS["User-Agent"])
                page = await context.new_page()
                response = await page.goto(url, timeout=self.timeout_sec * 1000, wait_until="domcontentloaded")
                content = await page.content()
                await browser.close()
                return {
                    "success": True,
                    "status_code": response.status if response else 200,
                    "content": content,
                    "url": url,
                    "error": None
                }
        except Exception as e:
            # Fallback to HTTP
            return self.fetch_url_http(url)
