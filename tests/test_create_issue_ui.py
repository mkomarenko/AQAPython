import pytest

from src.pages.create_issue_page import JiraCreateIssuePage
from src.pages.login_page import JiraLoginPage
from src.pages.main_page import JiraMainPage
from tests.base_test import BaseTest

from globals.jira_globals import *


@pytest.mark.usefixtures("jira_cleanup")
class TestCreateIssueUI(BaseTest):

    project_name = "AQAPython (AQAPYTHON)"

    test_data = [
        ("Maxim test issue 1", "Bug"),
        ("Maxim test issue 2", "User Story"),
        ("Maxim test issue 3", "Test"),
        ("Maxim test issue 4", "Task"),
        ("Maxim test issue 2", "Story")
    ]

    def setup_method(self):
        self.login_page = JiraLoginPage(self.driver, self.wait)
        self.main_page = JiraMainPage(self.driver, self.wait)
        self.create_issue_page = JiraCreateIssuePage(self.driver, self.wait)

    def test_login(self):
        self.login_page.open()
        self.login_page.login(login, password)
        assert self.main_page.at_page()

    @pytest.mark.parametrize("summary, issue_type", test_data)
    def test_create_issue(self, summary, issue_type):
        self.main_page.open_create_issue_page()
        assert self.create_issue_page.at_page()
        self.create_issue_page.create_jira_issue(self.project_name, issue_type, summary)
        assert summary in self.main_page.issue_link_text()
        assert self.main_page.at_page()



