from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://localhost:8000/index.html.html")
    page.locator(".btn.go").first.hover()
    page.screenshot(path="hover.png")
    browser.close()
