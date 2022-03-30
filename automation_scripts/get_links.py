from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import sys

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://piratebayorg.net")

    page.fill("#home > main > section > form > div:nth-child(1) > input[type=search]", sys.argv[1])
    page.click("#home > main > section > form > div:nth-child(3) > input[type=submit]:nth-child(1)")
    page.is_visible("#st > span.item-icons > a")

    html = page.inner_html("#torrents")
    soup = BeautifulSoup(html, "html.parser")
    entries = soup.find_all(id="st")

    if len(sys.argv)==3:
        tries = int(sys.argv[2])
    else:
        tries = 3

    for i in range(tries):
        name = entries[i].find(class_="list-item item-name item-title").a.text
        size = entries[i].find(class_="list-item item-size").text
        link = entries[i].find(class_="item-icons").a['href']

        payload = f"\nName: {name}\nSize: {size}\nLink: {link}\n"
        print(payload) 

    