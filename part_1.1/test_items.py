import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
expected_button_text = {
    'ru': 'Добавить в корзину',
    'en-gb': 'Add to basket'
}


def test_guest_should_see_login_link(browser, language):
    # Arrange
    browser.get(link)

    # Act
    basket_button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    lang_of_page = browser.find_element(By.CSS_SELECTOR, '[class="no-js"]').get_attribute("lang")

    # Assert
    assert basket_button.text in expected_button_text[language], "Неверное содержание текста кнопки"
    assert lang_of_page == language, "Неверный язык страницы"
