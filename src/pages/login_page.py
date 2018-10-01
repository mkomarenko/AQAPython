from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from globals.jira_globals import base_url
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    URL = base_url
    LOGIN_INPUT = (By.ID, "login-form-username")
    PASSWORD_INPUT = (By.ID, "login-form-password")
    LOGIN_BUTTON = (By.ID, "login")

    def open(self):
        self.driver.get(self.URL)
        return self

    def at_page(self):
        return "System Dashboard - Hillel IT School JIRA" in self.driver.title

    def login(self, username, password):
        self.type_username(username)
        self.type_password(password)
        self.submit_login()

    def type_username(self, username):
        login_input = self.wait.until(EC.visibility_of_element_located(self.LOGIN_INPUT))
        login_input.clear()
        login_input.send_keys(username)

    def type_password(self, password):
        password_input = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

    def submit_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def is_username_error_displayed(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "usernameerror"))).is_displayed()

    def get_username_error_text(self):
        return self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'aui-message')]/p"))).text
