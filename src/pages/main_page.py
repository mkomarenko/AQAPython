from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage


class JiraMainPage(BasePage):
    URL = "http://jira.hillel.it:8080/secure/Dashboard.jspa"
    CREATE_BUTTON = (By.ID, "create_link")
    ISSUE_LINK = (By.CSS_SELECTOR, "a.issue-created-key.issue-link")
    BLANKET_DIV = (By.XPATH, "//body/div[contains(@class, 'aui-blanket')]")

    def open(self):
        self.driver.get(self.URL)
        return self

    def at_page(self):
        return self.wait.until(EC.visibility_of_element_located(self.CREATE_BUTTON)).is_displayed()

    def open_create_issue_page(self):
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, "//body/div[contains(@class, 'aui-blanket')]")))
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.aui-flag")))
        self.wait.until(EC.element_to_be_clickable(self.CREATE_BUTTON)).click()

    def issue_link_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ISSUE_LINK)).text




