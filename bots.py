# bot.py
from playwright.sync_api import sync_playwright

links = [
    "https://youtu.be/bW9jdtw--Hc",
    "https://youtu.be/Zg8Oe9qwInw",
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for url in links:
        try:
            page.goto(url, timeout=30000)
            page.wait_for_timeout(3000)
            print(url, "->", page.title())
        except Exception as e:
            print(url, "-> error:", e)

    browser.close()