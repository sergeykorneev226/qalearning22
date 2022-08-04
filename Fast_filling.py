import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/huge_form.html"

try:

    driver = webdriver.Chrome()
    driver.get(link1)

    elements = driver.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Ответ")

    enter_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    enter_button.click()

finally:

    time.sleep(10)
    driver.quit()



