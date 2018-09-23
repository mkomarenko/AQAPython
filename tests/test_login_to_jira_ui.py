from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.jira_login_page import JiraLoginPage
from src.pages.jira_main_page import JiraMainPage
from tests.base_test import BaseTest


class TestJiraLoginUI(BaseTest):

    def test_login_page(self):
        self.login_page = JiraLoginPage(self.driver, self.wait)
        self.main_page = JiraMainPage(self.driver, self.wait)
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.login("Maksym_Komarenko", "Mk810426@odsu_")
        assert self.main_page.at_page()
