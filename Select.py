import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

driver = webdriver.Firefox()
driver.get(link)

a = int(driver.find_element(By.ID, "num1").text)
b = int(driver.find_element(By.ID, "num2").text)
x = a + b

# x = 0
#
# def calc(x):
#     x = a + b
#     return x

a = int(driver.find_element(By.ID, "num1").text)
b = int(driver.find_element(By.ID, "num2").text)

# y = calc(x)


select = Select(driver.find_element(By.ID, "dropdown")).select_by_value(str(x))

submit = driver.find_element(By.XPATH, "/html/body/div/form/button")
submit.click()

time.sleep(10)
driver.quit()

