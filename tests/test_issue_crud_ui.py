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

    @pytest.mark.parametrize("summary, issue_type", test_data)
    def test_create_issue(self, get_main_page, get_new_issue_page, summary, issue_type):
        with allure.step("Opening main page"):
            main_page = get_main_page
            main_page.open()
            assert main_page.at_page()
        with allure.step("Opening create new issue dialog"):
            main_page.open_create_issue_page()
            new_issue_page = get_new_issue_page
            assert new_issue_page.at_page()
        with allure.step("Creating new issue"):
            new_issue_page.create_issue(self.project_name, issue_type, summary)
            assert summary in main_page.issue_link_text()

    def test_empty_summary(self, get_main_page, get_new_issue_page):
        summary = ""
        with allure.step("Opening create new issue dialog"):
            main_page = get_main_page
            main_page.open_create_issue_page()
            new_issue_page = get_new_issue_page
            assert new_issue_page.at_page()
        with allure.step("Trying to create an issue with empty summary"):
            new_issue_page.type_summary(summary)
            new_issue_page.submit_issue()
            assert "You must specify a summary of the issue" in new_issue_page.error_text()
        with allure.step("Canceling new issue dialog"):
            new_issue_page.cancel_issue()
            assert main_page.at_page()

    def test_summary_longer_than_supported(self, get_main_page, get_new_issue_page):
        summary = "Maxim " * 50
        with allure.step("Opening create new issue dialog"):
            main_page = get_main_page
            main_page.open_create_issue_page()
            new_issue_page = get_new_issue_page
            assert new_issue_page.at_page()
        with allure.step("Trying to create an issue with not supported summary"):
            new_issue_page.type_summary(summary)
            new_issue_page.submit_issue()
            assert "Summary must be less than 255 characters" in new_issue_page.error_text()
        with allure.step("Canceling new issue dialog"):
            new_issue_page.cancel_issue()
            assert main_page.at_page()

    def test_search_five_issues(self, get_search_page):
        with allure.step("Opening search issues page"):
            search_page = get_search_page
            search_page.open()
            assert search_page.at_page()
        with allure.step("Searching 5 issues"):
            search_page.search_by_text("Maxim test issue")
            assert "5" == search_page.total_number_of_issues()

    def test_search_one_issues(self, get_search_page):
        with allure.step("Opening search issues page"):
            search_page = get_search_page
            search_page.open()
            assert search_page.at_page()
        with allure.step("Searching 1 issue"):
            search_page.search_by_text("Maxim test issue 1")
            assert "1" == search_page.total_number_of_issues()

    def test_update_issue(self, get_search_page, get_issue_summary_page, get_edit_issue_page):
        summary = "Maxim test issue 1"
        new_prio = "Medium"
        new_assignee = "Maksym_Komarenko"
        new_summary = "Updated: " + summary
        with allure.step("Opening issue summary page"):
            search_page = get_search_page
            issue_summary_page = get_issue_summary_page
            search_page.open_issue_with_summary(summary)
            assert issue_summary_page.at_page()
        with allure.step("Opening edit issue dialog"):
            issue_summary_page.open_edit_issue()
            edit_issue_page = get_edit_issue_page
            assert edit_issue_page.at_page()
        with allure.step("Editing and save issue"):
            edit_issue_page.type_summary(new_summary)
            edit_issue_page.type_priority(new_prio)
            edit_issue_page.type_assignee(new_assignee)
            edit_issue_page.submit_update()
            assert new_summary in issue_summary_page.get_summary_val()
            assert new_prio in issue_summary_page.get_priority_val()










