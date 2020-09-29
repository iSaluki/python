# Requires Selenium and a Selenium webdriver for your device

from selenium import webdriver

url = input("Enter URL: ")

driver = webdriver.Chrome()
driver.get(url)
