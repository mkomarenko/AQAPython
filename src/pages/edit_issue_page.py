import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class EditIssuePage(BasePage):
    SUMMARY_INPUT = (By.ID, "summary")
    ISSUE_TYPE_INPUT = (By.ID, "issuetype-field")
    PRIORITY_INPUT = (By.ID, "priority-field")
    ASSIGNEE_INPUT = (By.ID, "assignee-field")
    UPDATE_BUTTON = (By.ID, "edit-issue-submit")

    def at_page(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUMMARY_INPUT)).is_displayed()

    def get_summary(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUMMARY_INPUT)).get_attribute("value")

    def type_summary(self, summary):
        summary_elem = self.wait.until(EC.visibility_of_element_located(self.SUMMARY_INPUT))
        summary_elem.clear()
        summary_elem.send_keys(summary)

    def type_priority(self, summary):
        prio_elem = self.wait.until(EC.element_to_be_clickable(self.PRIORITY_INPUT))
        prio_elem.click()
        prio_elem = self.wait.until(EC.element_to_be_clickable(self.PRIORITY_INPUT))
        prio_elem.send_keys(summary)
        prio_elem.send_keys(Keys.RETURN)

    def type_assignee(self, summary):
        assignee_elem = self.wait.until(EC.element_to_be_clickable(self.ASSIGNEE_INPUT))
        assignee_elem.click()
        assignee_elem = self.wait.until(EC.element_to_be_clickable(self.ASSIGNEE_INPUT))
        assignee_elem.send_keys(summary)
        # assignee_elem.send_keys(Keys.RETURN)

    def submit_update(self):
        self.wait.until(EC.element_to_be_clickable(self.UPDATE_BUTTON)).click()

    def update_issue(self, summary, priority, assignee):
        self.type_summary(summary)
        time.sleep(1)
        self.type_priority(priority)
        time.sleep(1)
        self.type_assignee(assignee)
        time.sleep(1)
        self.submit_update()
        time.sleep(2)
