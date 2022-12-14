from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
browser = None


def setup_function():
    print("start browser for test..")
    global browser
    browser = webdriver.Chrome()


def teardown_function():
    print("quit browser for test..")
    browser.quit()


def test_guest_should_see_login_link():
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


def test_guest_should_see_basket_link_on_the_main_page():
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
