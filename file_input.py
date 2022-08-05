import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/file_input.html'


driver = webdriver.Firefox()
driver.get(link)


first_name = driver.find_element(By.NAME, "firstname")
first_name.send_keys("Ivan")

second_name = driver.find_element(By.NAME, "lastname")
second_name.send_keys("Ivanov")

email = driver.find_element(By.NAME, "email")
email.send_keys("ivan@gmail.com")

file = driver.find_element(By.ID, "file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')
file.send_keys(file_path)

submit = driver.find_element(By.XPATH, "/html/body/div/form/button")
submit.click()


time.sleep(5)
driver.quit()


