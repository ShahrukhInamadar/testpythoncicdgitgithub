from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_google_search():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")
    time.sleep(2)
    
    driver.quit()