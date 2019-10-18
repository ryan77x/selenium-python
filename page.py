from base_page import BasePage
from locators import AdminLoginPageLocators

class AdminLoginPage(BasePage):

    def input_user_name(self, user_name):
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys(user_name)

    def input_password(self, password):
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)

    def click_login_button(self):
        element = self.driver.find_element(*AdminLoginPageLocators.LOGIN_BUTTON)
        element.click()

    def get_invalid_login_alert_message(self):
        element = self.driver.find_element(*AdminLoginPageLocators.LOGIN_RESULT_ALERT_TEXT)
        return element.text

    def get_invalid_email_format_alert_message(self):
        element = self.driver.find_element(*AdminLoginPageLocators.LOGIN_RESULT_ALERT_TEXT)
        return element.text


class AdminPage(BasePage):
    pass