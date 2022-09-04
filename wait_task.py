import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'

driver = webdriver.Firefox()
driver.get(link)

wait = WebDriverWait(driver, 5)
price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button = driver.find_element(By.ID, "book")
button.click()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_elt = driver.find_element(By.ID, "input_value")
x = x_elt.text
y = calc(x)

text_field = driver.find_element(By.ID, "answer")
text_field.send_keys(y)

submit = driver.find_element(By.ID, "solve")
submit.click()

time.sleep(10)

driver.quit()
