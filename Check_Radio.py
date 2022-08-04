import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/math.html'



try:

    driver = webdriver.Firefox()
    driver.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_elt = driver.find_element(By.ID, "input_value")
    x = x_elt.text
    y = calc(x)

    text_field = driver.find_element(By.ID, "answer")
    text_field.send_keys(y)

    checkbox = driver.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = driver.find_element(By.ID, "robotsRule")
    radio.click()

    submit = driver.find_element(By.XPATH, "/html/body/div/form/button")
    submit.click()

    # time.sleep(1)
    # welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # welcome_text = welcome_text_elt.text
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)
    driver.quit()


