import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/find_link_text"

try:

    driver = webdriver.Chrome()
    driver.get(link1)

    text_link_crypto = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    link2 = driver.find_element(By.LINK_TEXT, text_link_crypto).get_attribute('href')
    driver.get(link2)
    time.sleep(5)

finally:
    driver.quit()

