# Selenium tutorial
from selenium import webdriver

PATH = "C:\\Selenium_drivers\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
driver.quit()