from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def play():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://demo.opencart.com/admin/")
        page.fill("input#input-username","demo")
        page.fill("input#input-password","demo")
        page.click("button[type=submit]")
        html = page.inner_html("#content")
        soup = BeautifulSoup(html,"html.parser")
        total_orders = soup.find("h2",{"class":"pull-right"}).text
        print("Total orders = ",total_orders)
        browser.close()

if __name__=="__main__":
    play()