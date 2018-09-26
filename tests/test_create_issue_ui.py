from src.pages.create_issue_page import JiraCreateIssuePage
from src.pages.login_page import JiraLoginPage
from src.pages.main_page import JiraMainPage
from tests.base_test import BaseTest

from globals.jira_globals import *


class TestCreateIssueUI(BaseTest):

    def setup_method(self):
        self.login_page = JiraLoginPage(self.driver, self.wait)
        self.main_page = JiraMainPage(self.driver, self.wait)
        self.create_issue_page = JiraCreateIssuePage(self.driver, self.wait)

    def test_create_issue(self):
        summary = "Maxim test"
        self.login_page.open()
        self.login_page.login(login, password)
        self.main_page.open_create_issue_page()
        assert self.create_issue_page.at_page()
        self.create_issue_page.create_jira_issue("AQAPython (AQAPYTHON)", "Bug", summary)
        assert self.main_page.is_issue_link_displayed()



