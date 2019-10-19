from base_page import BasePage
from selenium.webdriver.common.by import By

class AdminLoginPage(BasePage):
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    login_result_alert_message = (By.CSS_SELECTOR, "div.resultlogin")

    def input_user_name(self, user_name):
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys(user_name)

    def input_password(self, password):
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)

    def click_login_button(self):
        element = self.driver.find_element(*self.login_button)
        element.click()

    def login(self, user_name, password):
        self.input_user_name(user_name)
        self.input_password(password)
        self.click_login_button()

    def get_invalid_login_alert_message(self):
        element = self.driver.find_element(*self.login_result_alert_message)
        return element.text


class AdminPage(BasePage):
    pass