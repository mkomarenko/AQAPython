import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage


class CreateIssuePage(BasePage):
    PROJECT_INPUT = (By.ID, "project-field")
    PROJECT_DROPDOWN = (By.CSS_SELECTOR, "span.icon.aui-ss-icon.noloading.drop-menu")
    ISSUE_TYPE_INPUT = (By.ID, "issuetype-field")
    ISSUE_TYPE_DROPDOWN = (By.ID, "issuetype")
    SUMMARY_INPUT = (By.ID, "summary")
    DESCRIPTION_FIELD = (By.ID, "description")
    SUBMIT_BUTTON = (By.ID, "create-issue-submit")
    CANCEL_LINK = (By.CSS_SELECTOR, "a.cancel")
    ERROR_DIV = (By.CSS_SELECTOR, "div.error")

    def at_page(self):
        return self.wait.until(EC.visibility_of_element_located(self.PROJECT_INPUT)).is_displayed()

    def select_project(self, project_name):
        project_elem = self.wait.until(EC.element_to_be_clickable(self.PROJECT_INPUT))
        project_elem.clear()
        project_elem.send_keys(project_name)
        project_elem.send_keys(Keys.RETURN)
        time.sleep(1)

    def select_issue_type(self, issue_type):
        issue_elem = self.wait.until(EC.element_to_be_clickable(self.ISSUE_TYPE_INPUT))
        issue_elem.clear()
        issue_elem.send_keys(issue_type)
        issue_elem.send_keys(Keys.RETURN)
        time.sleep(1)

    def type_summary(self, summary):
        summary_elem = self.wait.until(EC.element_to_be_clickable(self.SUMMARY_INPUT))
        summary_elem.clear()
        summary_elem.send_keys(summary)

    def submit_issue(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def cancel_issue(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCEL_LINK)).click()
        self.driver.switch_to.alert.accept()
        time.sleep(1)

    def create_issue(self, project_name, issue_type, summary):
        self.select_project(project_name)
        self.select_issue_type(issue_type)
        self.type_summary(summary)
        self.submit_issue()
        time.sleep(1)

    def error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_DIV)).text
