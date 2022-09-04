import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_guest_should_see_correct_text(browser):
    correct_text = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button").text
    assert "Add to basket" or "Добавить в корзину" in correct_text, "Text is not correct"
