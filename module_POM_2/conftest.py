import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language: en-gb or ru")


# Фикстура, подготавливающая и закрывающая окружение
@pytest.fixture(scope="function")
def browser(language):
    print(f'\nstart {language} version..')

    options = Options()
    options.add_experimental_option('prefs', {'int1.accept_languages': language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="session")
def language(request):
    return request.config.getoption("language")
