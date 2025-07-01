# render.py

from playwright.sync_api import sync_playwright

URL = "https://store.steampowered.com/specials"


def render_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)

        # Wait until all network activity settles
        page.wait_for_load_state("networkidle")

        # Scroll to bottom (twice for good measure)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(3000)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(3000)

        html = page.content()
        browser.close()
        return html
