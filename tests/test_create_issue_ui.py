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
        ("Maxim test issue 5", "Story")
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

    def test_empty_summary(self):
        issue_type = "Bug"
        summary = ""
        self.main_page.open_create_issue_page()
        assert self.create_issue_page.at_page()
        self.create_issue_page.create_jira_issue(self.project_name, issue_type, summary)
        assert "You must specify a summary of the issue" in self.create_issue_page.error_text()
        self.create_issue_page.cancel_issue()
        assert self.main_page.at_page()

    def test_summary_longer_than_supported(self):
        issue_type = "Bug"
        summary = "Maxim " * 50
        self.main_page.open_create_issue_page()
        assert self.create_issue_page.at_page()
        self.create_issue_page.create_jira_issue(self.project_name, issue_type, summary)
        assert "Summary must be less than 255 characters" in self.create_issue_page.error_text()
        self.create_issue_page.cancel_issue()
        assert self.main_page.at_page()




