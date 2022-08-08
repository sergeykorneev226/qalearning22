import time
import os
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/redirect_accept.html'

driver = webdriver.Firefox()
driver.get(link)

button = driver.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
button.click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

time.sleep(1)

x_elt = driver.find_element(By.ID, "input_value")
x = x_elt.text
y = calc(x)

text_field = driver.find_element(By.ID, "answer")
text_field.send_keys(y)

submit = driver.find_element(By.XPATH, "/html/body/form/div/div/button")
submit.click()

time.sleep(1)
driver.quit()
