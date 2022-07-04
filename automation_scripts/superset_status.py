#!/usr/bin/env python3

from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

def main() -> int:
    if not EMAIL or not PASSWORD:
        print('EMAIL and or PASSWORD not in environment variables')
        print('Please check .env')
        return 1

    with sync_playwright() as p:
        print('Launching browser...')
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://app.joinsuperset.com/#/s/jobprofiles')
        page.fill('//*[@id="email"]', EMAIL)
        page.fill('//*[@id="password"]', PASSWORD)
        print('Logging into Superset...')
        page.click('//*[@id="login-cloak"]/div/div[2]/div[3]/form[1]/input')
        print('Parsing page...\n')
        result = page.locator('//*[@id="app-ui-view"]/div/div/div[2]/div/div[4]/div/div/table/tbody/tr/td[7]/div/div/span[1]/strong').text_content()
        print(f'Cognizant PAT status: {result}\n')
        context.close()
        browser.close()
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
