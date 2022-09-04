import pytest
from selenium import webdriver


link_en = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
link_ru = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language_type', action='store', default="en",
                     help="Choose language: english or russian")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language_type = request.config.getoption("language_type")
    browser = None
    if browser_name == "chrome" and language_type == "en":
        print("\nstart chrome browser for test on en..")
        browser = webdriver.Chrome()
        browser.get(link_en)
    elif browser_name == "chrome" and language_type == "ru":
        print("\nstart chrome browser for test on ru..")
        browser = webdriver.Chrome()
        browser.get(link_ru)
    elif browser_name == "firefox" and language_type == "en":
        print("\nstart firefox browser for test on en..")
        browser = webdriver.Firefox()
        browser.get(link_en)
    elif browser_name == "firefox" and language_type == "ru":
        print("\nstart firefox browser for test on ru..")
        browser = webdriver.Firefox()
        browser.get(link_ru)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
