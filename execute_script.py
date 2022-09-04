import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/execute_script.html'


driver = webdriver.Firefox()
driver.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_elt = driver.find_element(By.ID, "input_value")
x = x_elt.text
y = calc(x)

button = driver.find_element(By.TAG_NAME, "button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)


text_field = driver.find_element(By.ID, "answer")
text_field.send_keys(y)

checkbox = driver.find_element(By.ID, "robotCheckbox")
checkbox.click()

radio = driver.find_element(By.ID, "robotsRule")
radio.click()

submit = driver.find_element(By.XPATH, "/html/body/div/form/button")
submit.click()


time.sleep(5)
driver.quit()


