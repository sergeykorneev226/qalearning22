import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/get_attribute.html'

try:

    driver = webdriver.Firefox()
    driver.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_elt = driver.find_element(By.ID, "treasure")
    x = x_elt.get_attribute("valuex")
    y = calc(x)

    text_field = driver.find_element(By.ID, "answer")
    text_field.send_keys(y)

    checkbox = driver.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = driver.find_element(By.ID, "robotsRule")
    radio.click()

    submit = driver.find_element(By.XPATH, "/html/body/div/form/div/div/button")
    submit.click()

finally:

    time.sleep(10)
    driver.quit()



# people_radio = driver.find_element(By.ID, "robotsRule")
# people_checked = people_radio.get_attribute("checked")
# print("value of people radio: ", people_checked)
# assert people_checked is not None, "People radio is not selected by default"
