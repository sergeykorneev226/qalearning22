
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest

link = "http://selenium1py.pythonanywhere.com/"


# @pytest.fixture(scope="module")
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


# вызываем фикстуру в тесте, передав ее как параметр
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


def test_guest_should_see_basket_link_on_the_main_page(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
