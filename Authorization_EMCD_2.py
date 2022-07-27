import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://emcd.io/pool/dashboard/login")
print(driver.title)

username = driver.find_element(By.NAME, "email")
username.send_keys("sergeykorneev226@gmail.com")

password = driver.find_element(By.NAME, "password")
password.send_keys("2987768Qwerty@1")

enter_button = driver.find_element(By.CLASS_NAME, "el-button")
enter_button.click()
time.sleep(5)

url = driver.current_url

if url == "https://emcd.io/pool/dashboard/":
    print("Successful authentication!")
else:
    print("Failed authentication:(")

driver.quit()
