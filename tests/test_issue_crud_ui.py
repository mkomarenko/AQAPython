import pytest

from globals.jira_globals import *
from src.pages.create_issue_page import CreateIssuePage
from src.pages.edit_issue_page import EditIssuePage
from src.pages.issue_summary_page import IssueSummaryPage
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage
from src.pages.search_page import SearchPage
from tests.base_test import BaseTest


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
        self.login_page = LoginPage(self.driver, self.wait)
        self.main_page = MainPage(self.driver, self.wait)
        self.create_issue_page = CreateIssuePage(self.driver, self.wait)
        self.search_page = SearchPage(self.driver, self.wait)
        self.issue_summary_page = IssueSummaryPage(self.driver, self.wait)
        self.edit_issue_page = EditIssuePage(self.driver, self.wait)

    def test_login(self):
        self.login_page.open()
        self.login_page.login(login, password)
        assert self.main_page.at_page()

    @pytest.mark.parametrize("summary, issue_type", test_data)
    def test_create_issue(self, summary, issue_type):
        self.driver.get_screenshot_as_file("screenshot/" + summary + ".png")
        self.main_page.open_create_issue_page()
        assert self.create_issue_page.at_page()
        self.create_issue_page.create_issue(self.project_name, issue_type, summary)
        assert summary in self.main_page.issue_link_text()
        assert self.main_page.at_page()

    def test_empty_summary(self):
        summary = ""
        self.driver.get_screenshot_as_file("screenshot/empty_summary.png")
        self.main_page.open_create_issue_page()
        assert self.create_issue_page.at_page()
        self.create_issue_page.type_summary(summary)
        self.create_issue_page.submit_issue()
        assert "You must specify a summary of the issue" in self.create_issue_page.error_text()
        self.create_issue_page.cancel_issue()
        assert self.main_page.at_page()

    def test_summary_longer_than_supported(self):
        summary = "Maxim " * 50
        self.driver.get_screenshot_as_file("screenshot/long_summary.png")
        self.main_page.open_create_issue_page()
        assert self.create_issue_page.at_page()
        self.create_issue_page.type_summary(summary)
        self.create_issue_page.submit_issue()
        assert "Summary must be less than 255 characters" in self.create_issue_page.error_text()
        self.create_issue_page.cancel_issue()
        assert self.main_page.at_page()

    def test_search_five_issues(self):
        self.search_page.open()
        assert self.search_page.at_page()
        self.driver.get_screenshot_as_file("screenshot/search_5_issues.png")
        self.search_page.search_by_text("Maxim test issue")
        assert "5" == self.search_page.total_number_of_issues()

    def test_search_one_issues(self):
        self.search_page.open()
        assert self.search_page.at_page()
        self.driver.get_screenshot_as_file("screenshot/search_1_issue.png")
        self.search_page.search_by_text("Maxim test issue 1")
        assert "1" == self.search_page.total_number_of_issues()

    def test_update_issue(self):
        new_prio = "Medium"
        new_assignee = "Maksym_Komarenko"
        self.driver.get_screenshot_as_file("screenshot/open_issue_with_suumary.png")
        self.search_page.open_issue_with_summary("Maxim test issue 1")
        assert self.issue_summary_page.at_page()
        self.issue_summary_page.open_edit_issue()
        assert self.edit_issue_page.at_page()
        new_summary = "Updated: " + self.edit_issue_page.get_summary()
        self.edit_issue_page.type_summary(new_summary)
        self.edit_issue_page.type_priority(new_prio)
        self.edit_issue_page.type_assignee(new_assignee)
        self.edit_issue_page.submit_update()
        assert new_summary in self.issue_summary_page.get_summary_val()
        assert new_prio in self.issue_summary_page.get_priority_val()










