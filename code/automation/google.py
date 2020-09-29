from selenium import webdriver
from selenium.webdriver.common.keys import Keys

query = input("What would you like to search? ")


driver = webdriver.Chrome()
driver.get("https://google.com/")
search_bar = driver.find_element_by_name("q")
search_bar.send_keys(query)
search_bar.send_keys(Keys.ENTER)

