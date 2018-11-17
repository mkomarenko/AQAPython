import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from globals.jira_globals import base_url
from src.pages.base_page import BasePage


class SearchPage(BasePage):
    URL = base_url + "/issues/?jql="
    TITLE_HEADER = (By.CSS_SELECTOR, "h1.search-title")
    QUERY_INPUT = (By.ID, "searcher-query")
    ISSUE_TABLE = (By.ID, "issuetable")
    ISSUE_LINK = (By.CSS_SELECTOR, "a.issue-link")
    SPLIT_ISSUE_LINK = (By.CSS_SELECTOR, "a.splitview-issue-link")
    RESULT_COUNT_TEXT = (By.CLASS_NAME, "showing")
    RESULT_COUNT = (By.CSS_SELECTOR, ".results-count-total.results-count-link")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.aui-button.aui-button-subtle.search-button")

    def open(self):
        self.driver.get(self.URL)
        return self

    def at_page(self):
        return self.wait.until(EC.presence_of_element_located(self.QUERY_INPUT)).is_enabled()

    def type_query(self, text):
        query_elem = self.wait.until(EC.visibility_of_element_located(self.QUERY_INPUT))
        query_elem.clear()
        query_elem.send_keys(text)

    def submit_query(self):
        search_button_elem = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search_button_elem.click()

    def search_by_text(self, text):
        self.type_query(text)
        self.submit_query()
        time.sleep(2)

    def total_number_of_issues(self, expected_number):
        result_elem = self.wait.until(EC.visibility_of_element_located(self.RESULT_COUNT))
        # g = re.compile(" of (\d{1,10})").search(result_elem.text)
        total_count = int(result_elem.text)
        # if g:
        #    total_count = int(g.group(1))
        # else:
        #    print("No matches found")
        return total_count == expected_number

    def open_issue_with_summary(self, summary):
        self.search_by_text(summary)
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, summary))).click()

