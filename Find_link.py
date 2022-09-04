import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/find_link_text"

driver = webdriver.Firefox()
driver.get(link1)

text_link_crypto = str(math.ceil(math.pow(math.pi, math.e) * 10000))
link2 = driver.find_element(By.LINK_TEXT, text_link_crypto).get_attribute('href')
driver.get(link2)

first_name = driver.find_element(By.NAME, "first_name")
first_name.send_keys("Ivan")
last_name = driver.find_element(By.NAME, "last_name")
last_name.send_keys("Ivanov")
city = driver.find_element(By.CSS_SELECTOR, ".form-control.city")
city.send_keys("Smolensk")
country = driver.find_element(By.ID, "country")
country.send_keys("Russia")

enter_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
enter_button.click()

time.sleep(10)
driver.save_screenshot('screenshot.png')
driver.quit()


