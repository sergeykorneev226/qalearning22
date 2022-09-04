import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('list_links', ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1", "236899/step/1", "236903/step/1", "236904/step/1", "236905/step/1"])
def test_guest_should_see_login_link(browser, list_links):
    link = f"https://stepik.org/lesson/{list_links}/"
    answer = math.log(int(time.time()))
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea").send_keys(answer)
    browser.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[4]/button").click()
    feedback = browser.find_element(By.XPATH, "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/div/div[1]/div[2]/div/p").text
    assert "Correct!" in feedback, "The answer is wrong"



