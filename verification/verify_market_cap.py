from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Load the local file - using /app prefix as seen in pwd
    page.goto("file:///app/index.html")

    # Click the Market Cap tab
    page.click("text=Market Cap")

    # Wait for the content to be visible
    page.wait_for_selector("#market-cap.active")

    # Wait a bit for the tables to render (they might be rendered by JS on load or tab switch)
    page.wait_for_timeout(2000)

    # Take a screenshot of the relevant section
    page.locator("#market-cap").screenshot(path="/home/jules/verification/market_cap_tab.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
