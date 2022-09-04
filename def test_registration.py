import time

from selenium import webdriver
from selenium.webdriver.common.by import By

main_page_link = "http://selenium1py.pythonanywhere.com/ru/"

login_locator = "#login_link"
email_locator = "#id_login-username"
password_locator = "#id_login-password"
button_locator = "/html/body/div[2]/div/div[2]/div[2]/div/div[1]/form/button"
result_page_locator = "/html/body/div[2]/div/div/div/div[1]/div/div"


def test_registration():
    # Data
    email = "ivan@gmail.com"
    password = "Qwerty@123"

    try:
        # Arrange
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get(main_page_link)

        # Act
        driver.find_element(By.CSS_SELECTOR, login_locator).click()
        driver.find_element(By.CSS_SELECTOR, email_locator).send_keys(email)
        driver.find_element(By.CSS_SELECTOR, password_locator).send_keys(password)
        driver.find_element(By.XPATH, button_locator).click()

        # Assert
        result_page = driver.find_element(By.XPATH, result_page_locator)
        assert "Рады видеть вас снова" in result_page.text, \
            "InputError"

    finally:
        time.sleep(5)
        driver.quit()


test_registration()
