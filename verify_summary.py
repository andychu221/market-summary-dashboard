from playwright.sync_api import sync_playwright
import time
import os

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})

        file_path = f"file://{os.path.abspath('index.html')}"
        page.goto(file_path)

        time.sleep(3)

        # Take a screenshot of the summary tab
        page.screenshot(path="verification/summary_tab_logo.png")

        browser.close()
        print("Summary screenshots saved.")

if __name__ == "__main__":
    verify()
