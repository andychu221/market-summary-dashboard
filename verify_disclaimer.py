from playwright.sync_api import sync_playwright
import time
import os

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})

        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        time.sleep(2)

        # Click the News tab using the onclick selector we found earlier
        page.click("div.tab-btn[onclick*='news']")
        time.sleep(2)

        # Wait for news items
        page.wait_for_selector(".list-item", timeout=10000)

        # Click the first news item
        page.click(".list-item:nth-child(1)")
        time.sleep(2)

        # Select the disclaimer element explicitly. It's a div with color: #888, font-size: 0.8rem at the bottom
        disclaimer = page.locator("#news-content > div").last
        disclaimer.scroll_into_view_if_needed()
        time.sleep(1)

        # Also take a full page screenshot just in case
        page.screenshot(path="verification/news_page_bottom.png")

        # And capture the disclaimer itself specifically
        disclaimer.screenshot(path="verification/news_disclaimer.png")

        browser.close()
        print("Disclaimer screenshots saved.")

if __name__ == "__main__":
    verify()
