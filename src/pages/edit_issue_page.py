import time

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class EditIssuePage(BasePage):
    SUMMARY_INPUT = (By.ID, "summary")
    ISSUE_TYPE_INPUT = (By.ID, "issuetype-field")
    UPDATE_BUTTON = (By.ID, "edit-issue-submit")

    def at_page(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUMMARY_INPUT)).is_displayed()

    def get_summary(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUMMARY_INPUT)).get_attribute("value")

    def type_summary(self, summary):
        summary_elem = self.wait.until(EC.visibility_of_element_located(self.SUMMARY_INPUT))
        summary_elem.clear()
        summary_elem.send_keys(summary)

    def submit_update(self):
        self.wait.until(EC.element_to_be_clickable(self.UPDATE_BUTTON)).click()

    def update_summary(self, summary):
        self.type_summary(summary)
        self.submit_update()
        time.sleep(2)
