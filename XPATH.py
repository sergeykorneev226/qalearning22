import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/find_xpath_form"

driver = webdriver.Firefox()
driver.get(link1)

first_name = driver.find_element(By.NAME, "first_name")
first_name.send_keys("Ivan")
last_name = driver.find_element(By.NAME, "last_name")
last_name.send_keys("Ivanov")
city = driver.find_element(By.CSS_SELECTOR, ".form-control.city")
city.send_keys("Smolensk")
country = driver.find_element(By.ID, "country")
country.send_keys("Russia")

enter_button = driver.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
enter_button.click()

time.sleep(10)
driver.quit()


