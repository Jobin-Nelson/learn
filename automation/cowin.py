from playwright.sync_api import Playwright, sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

PHONE_NUMBER = os.getenv('PHONE_NUMBER')

def run(playwright: Playwright) -> None:
    if not PHONE_NUMBER:
        print('PHONE_NUMBER is not in environment variables')
        print('Please check .env')
        return 
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://selfregistration.cowin.gov.in/")

    page.click("[placeholder=\"Enter\\ your\\ mobile\\ number\"]")
    page.fill("[placeholder=\"Enter\\ your\\ mobile\\ number\"]", PHONE_NUMBER)
    page.click("[aria-label=\"GET\\ OTP\"]")

    OTP = input("Please provide your OTP: ")
    page.fill("[placeholder=\"Enter\\ OTP\"]", OTP)
    with page.expect_navigation():
        page.click("[aria-label=\"Verify\\ \\&\\ Proceed\"]")

    with page.expect_navigation():
        page.click("text=Schedule")
    page.click("button[role=\"switch\"]")
    page.click("text=Select State Select District Search >> span")
    page.click("text=Kerala")
    page.click("#mat-select-value-3 span")
    page.click("text=Kollam")
    page.click("text=Kerala Select StateKollam Select District Search >> button")

    input("Press enter to close the browser")
    context.close()
    browser.close()

if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)
 
