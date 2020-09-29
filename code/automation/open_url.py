# Requires Selenium and a Selenium webdriver for your device

from selenium import webdriver
import time

url = input("Enter URL: ")

driver = webdriver.Chrome()
driver.get(url)
