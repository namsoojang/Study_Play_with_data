from selenium import webdriver
from selenium.common.exceptions import WebDriverException

browser = webdriver.Chrome()
browser.get("http://en.wikipedia.org")

browser.execute_script("alert('Hello, World!')")
