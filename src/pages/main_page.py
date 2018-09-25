from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage


class JiraMainPage(BasePage):
    URL = "http://jira.hillel.it:8080/secure/Dashboard.jspa"
    CREATE_BUTTON = (By.ID, "create_link")
    ISSUE_LINK = (By.CSS_SELECTOR, "a.issue-created-key.issue-link")

    def open(self):
        self.driver.get(self.URL)
        return self

    def at_page(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "create_link"))).is_displayed()

    def is_issue_link_displayed(self, summary):
        return self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[contains(text(), '" + summary + "') and contains(@class, 'issue-link')]"))).is_displayed()

    def open_create_issue_page(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "create_link")))
        self.driver.find_element(*self.CREATE_BUTTON).click()

