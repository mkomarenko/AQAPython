from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage


class JiraCreateIssuePage(BasePage):
    PROJECT_INPUT = (By.ID, "project-field")
    PROJECT_DROPDOWN = (By.ID, "project")
    ISSUE_TYPE_INPUT = (By.ID, "issuetype-field")
    ISSUE_TYPE_DROPDOWN = (By.ID, "issuetype")
    SUMMARY_INPUT = (By.ID, "summary")
    DESCRIPTION_FIELD = (By.ID, "description")
    SUBMIT_BUTTON = (By.ID, "create-issue-submit")
    CANCEL_LINK = (By.CSS_SELECTOR, "a.cancel")

    def at_page(self):
        return self.wait.until(EC.visibility_of_element_located(self.PROJECT_INPUT)).is_displayed()

    def select_project(self, project_name):
        input = self.wait.until(EC.element_to_be_clickable(self.PROJECT_INPUT))
        input.clear()
        input.send_keys(project_name)
        input.send_keys(Keys.RETURN)

    def select_issue_type(self, issue_type):
        input = self.wait.until(EC.element_to_be_clickable(self.ISSUE_TYPE_INPUT))
        input.clear()
        input.send_keys(issue_type)
        input.send_keys(Keys.RETURN)

    def type_summary(self, summary):
        summary_input = self.wait.until(EC.element_to_be_clickable(self.SUMMARY_INPUT))
        summary_input.clear()
        summary_input.send_keys(summary)

    def submit_issue(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def create_jira_issue(self, project_name, issue_type, summary):
        self.select_project(project_name)
        self.select_issue_type(issue_type)
        self.type_summary(summary)
        self.submit_issue()
