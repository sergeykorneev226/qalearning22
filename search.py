import time

from selenium import webdriver
from selenium.webdriver.common.by import By


main_page_link = "http://selenium1py.pythonanywhere.com/ru"

search_input_locator = "#id_q"
search_button_locator = "input.btn.btn-default"
result_page_title_locator = "h1"


def test_item_search():
    # Data
    search_text = "The shellcoder's handbook"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        search_input = browser.find_element(By.CSS_SELECTOR, search_input_locator)
        search_input.clear()

        # Act
        search_input.send_keys(search_text)
        browser.find_element(By.CSS_SELECTOR, search_button_locator).click()

        # Assert
        result_page_title = browser.find_element(By.CSS_SELECTOR, result_page_title_locator)
        assert search_text in result_page_title.text, \
            "Page title should contain searching item name"

    finally:
        time.sleep(5)
        browser.quit()

test_item_search()

