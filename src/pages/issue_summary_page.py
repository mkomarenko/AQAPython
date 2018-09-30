from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage


class IssueSummaryPage(BasePage):
    SUMMARY_HEADER = (By.ID, "summary-val")
    EDIT_BUTTON = (By.ID, "edit-issue")

    def at_page(self):
        return self.wait.until(EC.presence_of_element_located(self.SUMMARY_HEADER)).get_attribute(
            "title") == "Click to edit"

    def open_edit_issue(self):
        self.wait.until(EC.element_to_be_clickable(self.EDIT_BUTTON)).click()

    def get_summary_val(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUMMARY_HEADER)).text

