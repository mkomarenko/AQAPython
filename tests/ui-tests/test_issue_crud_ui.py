import allure
import pytest


@pytest.mark.ui_test
@pytest.mark.incremental
@pytest.mark.usefixtures("login_logout", "jira_cleanup")
class TestCRUDIssueUI:

    project_name = "AQAPython (AQAPYTHON)"

    test_data = [
        ("Maxim test issue 1", "Bug"),
        ("Maxim test issue 2", "User Story"),
        ("Maxim test issue 3", "Test"),
        ("Maxim test issue 4", "Task"),
        ("Maxim test issue 5", "Story")
    ]

    @allure.title("Create issue UI")
    @pytest.mark.parametrize("summary, issue_type", test_data)
    def test_create_issue(self, get_main_page, get_new_issue_page, summary, issue_type):
        with allure.step("Open main page"):
            get_main_page.open()
        with allure.step("Check that main page is opened"):
            assert get_main_page.at_page()
        with allure.step("Open new issue dialog"):
            get_main_page.open_create_issue_page()
        with allure.step("Check that new issue dialog is opened"):
            assert get_new_issue_page.at_page()
        with allure.step("Call create issue method"):
            get_new_issue_page.create_issue(self.project_name, issue_type, summary)
        assert summary in get_main_page.issue_link_text()

    @allure.title("Create issue UI with empty summary")
    def test_empty_summary(self, get_main_page, get_new_issue_page):
        summary = ""
        with allure.step("Open new issue dialog"):
            get_main_page.open_create_issue_page()
        with allure.step("Check that new issue dialog is opened"):
            assert get_new_issue_page.at_page()
        with allure.step("Call type summary method"):
            get_new_issue_page.type_summary(summary)
        with allure.step("Call submit issue method"):
            get_new_issue_page.submit_issue()
        with allure.step("Check that correct error message is displayed"):
            assert "You must specify a summary of the issue" in get_new_issue_page.error_text()
        with allure.step("Cancel new issue dialog"):
            get_new_issue_page.cancel_issue()
        with allure.step("Check that user is returned to main page"):
            assert get_main_page.at_page()

    @allure.title("Create issue UI with unsupported summary")
    def test_summary_longer_than_supported(self, get_main_page, get_new_issue_page):
        summary = "Maxim " * 50
        with allure.step("Open new issue dialog"):
            get_main_page.open_create_issue_page()
        with allure.step("Check that new issue dialog is opened"):
            assert get_new_issue_page.at_page()
        with allure.step("Call type summary method"):
            get_new_issue_page.type_summary(summary)
        with allure.step("Call submit issue method"):
            get_new_issue_page.submit_issue()
        with allure.step("Check that correct error message is displayed"):
            assert "Summary must be less than 255 characters" in get_new_issue_page.error_text()
        with allure.step("Cancel new issue dialog"):
            get_new_issue_page.cancel_issue()
        with allure.step("Check that user is returned to main page"):
            assert get_main_page.at_page()

    @allure.title("Search 5 issues UI")
    def test_search_five_issues(self, get_search_page):
        with allure.step("Open search issues page"):
            get_search_page.open()
        with allure.step("Check that search page is opened"):
            assert get_search_page.at_page()
        with allure.step("Call search by text method"):
            get_search_page.search_by_text("Maxim test issue")
        with allure.step("Check that number of found issues correct"):
            assert "5" == get_search_page.total_number_of_issues()

    @allure.title("Search 1 issue UI")
    def test_search_one_issues(self, get_search_page):
        with allure.step("Open search issues page"):
            get_search_page.open()
        with allure.step("Check that search page is opened"):
            assert get_search_page.at_page()
        with allure.step("Call search by text method"):
            get_search_page.search_by_text("Maxim test issue 1")
        with allure.step("Check that number of found issues correct"):
            assert "1" == get_search_page.total_number_of_issues()

    @allure.title("Update issue UI")
    def test_update_issue(self, get_search_page, get_issue_summary_page, get_edit_issue_page):
        summary = "Maxim test issue 1"
        new_prio = "Medium"
        new_assignee = "Maksym_Komarenko"
        new_summary = "Updated: " + summary
        with allure.step("Call open issue summary method"):
            get_search_page.open_issue_with_summary(summary)
        with allure.step("Check that issue summary page is opened"):
            assert get_issue_summary_page.at_page()
        with allure.step("Open edit issue dialog"):
            get_issue_summary_page.open_edit_issue()
        with allure.step("Check that edit issue dialog is opened"):
            assert get_edit_issue_page.at_page()
        with allure.step("Call update issue method"):
            get_edit_issue_page.update_issue(new_summary, new_prio, new_assignee)
        with allure.step("Check that new summary is displayed in issue summary"):
            assert new_summary in get_issue_summary_page.get_summary_val()
        with allure.step("Check that new priority is displayed in issue summary"):
            assert new_prio in get_issue_summary_page.get_priority_val()
