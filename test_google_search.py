from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import options

def test_google_search():
    # options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")

    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")

    assert "Google" in driver.title
    driver.quit()
