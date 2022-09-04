import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import argv

script_name, link = argv

try:

    driver = webdriver.Firefox()
    driver.get(link)

    first_name = driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    first_name.send_keys("Ivan")
    last_name = driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    last_name.send_keys("Ivanov")
    email = driver.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    email.send_keys("sergeykorneev226@gmail.com")

    enter_button = driver.find_element(By.XPATH, "/html/body/div/form/button")
    enter_button.click()

    time.sleep(1)
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)
    driver.quit()


