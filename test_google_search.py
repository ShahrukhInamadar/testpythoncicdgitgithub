# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common import options

# def test_google_search():
#     # options = Options()
#     # options.add_argument("--headless")
#     # options.add_argument("--disable-gpu")

#     # driver = webdriver.Chrome(options=options)
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.google.com")

#     time.sleep(2)
#     assert "Google" in driver.title
#     driver.quit()


import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@allure.title("Google Search Test")
@allure.description("Verify Google homepage opens")
@allure.severity(allure.severity_level.CRITICAL)
def test_google_search():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)

    with allure.step("Open Google"):
        driver.get("https://www.google.com")

    with allure.step("Verify title"):
        assert "Google" in driver.title

    driver.quit()
