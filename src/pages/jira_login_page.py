from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage


class JiraLoginPage(BasePage):
    URL = "http://jira.hillel.it:8080"
    LOGIN_INPUT = (By.ID, "login-form-username")
    PASSWORD_INPUT = (By.ID, "login-form-password")
    LOGIN_BUTTON = (By.ID, "login")

    def open(self):
        self.driver.get(self.URL)
        return self

    def at_page(self):
        return "System Dashboard - Hillel IT School JIRA" in self.driver.title

    def login(self, username, password):
        self.driver.find_element(*self.LOGIN_INPUT).clear()
        self.driver.find_element(*self.LOGIN_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).submit()

    def is_username_error_displayed(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "usernameerror"))).is_displayed()

