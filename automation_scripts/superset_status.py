from playwright.sync_api import sync_playwright
from creds import email, password

def main():
    with sync_playwright() as p:
        print('Launching browser...')
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://app.joinsuperset.com/#/s/jobprofiles')
        page.fill('//*[@id="email"]', email)
        page.fill('//*[@id="password"]', password)
        print('Logging into Superset...')
        page.click('//*[@id="login-cloak"]/div/div[2]/div[3]/form[1]/input')
        print('Parsing page...\n')
        result = page.locator('//*[@id="app-ui-view"]/div/div/div[2]/div/div[4]/div/div/table/tbody/tr/td[7]/div/div/span[1]/strong').text_content()
        print(f'Cognizant PAT status: {result}\n')
        browser.close()

if __name__ == '__main__':
    main()
