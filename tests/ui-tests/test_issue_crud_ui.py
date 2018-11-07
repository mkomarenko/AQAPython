import allure
import pytest

from globals.jira_globals import login
from src.pages.edit_issue_page import EditIssuePage
from src.pages.issue_summary_page import IssueSummaryPage
from src.pages.main_page import MainPage
from src.pages.search_page import SearchPage


@pytest.mark.ui_test
@pytest.mark.usefixtures("login_to_jira", "jira_test_data")
class TestCRUDIssueUI:

    project_name = "Webinar (WEBINAR)"

    test_data = [
        ("Maxim new issue test 1", "Bug"),
        ("Maxim new issue test 2", "User Story"),
        ("Maxim new issue test 3", "Test"),
        ("Maxim new issue test 4", "Task"),
        ("Maxim new issue test 5", "Story")
    ]

    @allure.title("Create issue UI")
    @pytest.mark.parametrize("summary, issue_type", test_data)
    def test_create_issue(self, browser, summary, issue_type):
        main_page = MainPage(browser)
        with allure.step("Open new issue dialog"):
            new_issue_page = main_page.open_create_issue_page()
            allure.attach(browser.get_screenshot_as_png(),
                          name="test_create_issue1",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Check that new issue dialog is opened"):
            assert new_issue_page.at_page()
        with allure.step("Call create issue method"):
            new_issue_page.create_issue(self.project_name, issue_type, summary)
        with allure.step("Check that issue link text contains issue summary"):
            assert main_page.issue_link_text(summary)
            allure.attach(browser.get_screenshot_as_png(),
                          name="test_create_issue2",
                          attachment_type=allure.attachment_type.PNG)

    @allure.title("Create issue UI negative (with empty summary)")
    def test_create_issue_empty_summary(self, browser):
        summary = ""
        issue_type = "Bug"
        main_page = MainPage(browser)
        with allure.step("Open new issue dialog"):
            new_issue_page = main_page.open_create_issue_page()
        with allure.step("Check that new issue dialog is opened"):
            assert new_issue_page.at_page()
        with allure.step("Call create issue method"):
            new_issue_page.create_issue(self.project_name, issue_type, summary)
        with allure.step("Check that correct error message is displayed"):
            assert new_issue_page.error_text("You must specify a summary of the issue")
            allure.attach(browser.get_screenshot_as_png(),
                          name="test_create_issue_empty_summary",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Cancel new issue dialog"):
            new_issue_page.cancel_issue()
        with allure.step("Check that user is returned to main page"):
            assert main_page.at_page()

    @allure.title("Create issue UI negative (with summary longer than supported)")
    def test_create_issue_unsupported_summary(self, browser):
        summary = "Maxim " * 50
        main_page = MainPage(browser)
        with allure.step("Open new issue dialog"):
            new_issue_page = main_page.open_create_issue_page()
        with allure.step("Check that new issue dialog is opened"):
            assert new_issue_page.at_page()
        with allure.step("Call type summary method"):
            new_issue_page.type_summary(summary)
        with allure.step("Call submit issue method"):
            new_issue_page.submit_issue()
        with allure.step("Check that correct error message is displayed"):
            assert new_issue_page.error_text("Summary must be less than 255 characters")
            allure.attach(browser.get_screenshot_as_png(),
                          name="test_create_issue_summary_longer_than_supported",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Cancel new issue dialog"):
            new_issue_page.cancel_issue()
        with allure.step("Check that user is returned to main page"):
            assert main_page.at_page()

    @allure.title("Search 5 issues UI")
    def test_search_five_issues(self, browser):
        search_page = SearchPage(browser)
        with allure.step("Open search issues page"):
            search_page.open()
        with allure.step("Check that search page is opened"):
            assert search_page.at_page()
        with allure.step("Call search by text method"):
            search_page.search_by_text("Maxim search issue")
        with allure.step("Check that number of found issues correct"):
            assert search_page.total_number_of_issues(5)
            allure.attach(browser.get_screenshot_as_png(),
                          name="test_search_five_issues",
                          attachment_type=allure.attachment_type.PNG)

    @allure.title("Search 1 issue UI")
    def test_search_one_issue(self, browser):
        search_page = SearchPage(browser)
        with allure.step("Open search issues page"):
            search_page.open()
        with allure.step("Check that search page is opened"):
            assert search_page.at_page()
        with allure.step("Call search by text method"):
            search_page.search_by_text("Maxim search issue 1")
        with allure.step("Check that number of found issues correct"):
            assert search_page.total_number_of_issues(1)
            allure.attach(browser.get_screenshot_as_png(),
                          name="test_search_one_issue",
                          attachment_type=allure.attachment_type.PNG)

    @allure.title("Update issue UI")
    def test_update_issue(self, browser):
        summary = "Maxim test issue 1"
        new_prio = "Medium"
        new_assignee = login
        new_summary = "Updated: " + summary
        search_page = SearchPage(browser)
        issue_summary_page = IssueSummaryPage(browser)
        edit_issue_page = EditIssuePage(browser)

        with allure.step("Open search issues page"):
            search_page.open()
        with allure.step("Check that search page is opened"):
            assert search_page.at_page()
        with allure.step("Call open issue summary method"):
            search_page.open_issue_with_summary(summary)
        with allure.step("Check that issue summary page is opened"):
            assert issue_summary_page.at_page()
        with allure.step("Open edit issue dialog"):
            issue_summary_page.open_edit_issue()
        with allure.step("Check that edit issue dialog is opened"):
            assert edit_issue_page.at_page()
        with allure.step("Call update issue method"):
            edit_issue_page.update_issue(new_summary, new_prio, new_assignee)
        with allure.step("Check that new summary is displayed in issue summary"):
            assert new_summary in issue_summary_page.get_summary_val()
        with allure.step("Check that new priority is displayed in issue summary"):
            assert new_prio in issue_summary_page.get_priority_val()
            allure.attach(browser.get_screenshot_as_png(),
                          name="test_update_issue",
                          attachment_type=allure.attachment_type.PNG)
