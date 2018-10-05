import pytest
import allure
from rest.jira_web_service import *


@pytest.mark.api_test
class TestIssueCRUD:
    created_issue_ids = []

    create_test_data = [
        ("Maxim test issue 1", "Maxim test issue", "Bug", "Low", "", 201,
         "'key': 'AQAPYTHON"),
        ("Maxim test issue 2", "Maxim test issue", "User Story", "High", "", 201,
         "'key': 'AQAPYTHON"),
        ("Maxim test issue 3", "Maxim test issue", "Test", "Medium", "", 201,
         "'key': 'AQAPYTHON"),
        ("Maxim test issue 4", "Maxim test issue", "Task", "Lowest", "", 201,
         "'key': 'AQAPYTHON"),
        ("Maxim test issue 5", "Maxim test issue", "Story", "Highest", "", 201,
         "'key': 'AQAPYTHON"),
        ("", "Maxim test issue", "Bug", "Low", "", 400,
         "You must specify a summary of the issue."),
        (
            "Maxim " * 50,
            "Maxim test issue", "Bug", "Low", "", 400, "Summary must be less than 255 characters."),
    ]

    search_test_data = [
        ("project = AQAPYTHON AND summary ~ 'Maxim test issue'",
         ["id", "key", "summary"], 200, 5),
        ("project = AQAPYTHON AND summary ~ 'Maxim test issue 1'",
         ["id", "key", "summary"], 200, 1),
        ("project = AQAPYTHON AND summary ~ 'Maxim test issue 123'",
         ["id", "key", "summary"], 200, 0),
    ]

    @allure.title("Create issue API")
    @pytest.mark.parametrize("summary, description, issue_type, priority, assignee, expected_sc, expected_text",
                             create_test_data)
    def test_issue_create(self, summary, description, issue_type, priority, assignee, expected_sc, expected_text):
        with allure.step("Sending API request"):
            r = JiraWebService.create_new_issue(summary, description, issue_type, priority, assignee)
            print("\nSTATUS CODE: " + str(r.status_code))
            print("\ndata: " + str(r.json()))
        with allure.step("Check response status code"):
            assert r.status_code == expected_sc
        if r.status_code == 201:
            with allure.step("Save id to created issues list"):
                self.created_issue_ids.append(r.json()['id'])
        with allure.step("Check response data content"):
            assert expected_text in str(r.json())

    @allure.title("Search issues API")
    @pytest.mark.parametrize("jql, fields, expected_sc, expected_count", search_test_data)
    def test_search_issue(self, jql, fields, expected_sc, expected_count):
        with allure.step("Sending API request"):
            r = JiraWebService.search_issues_by_jql(jql, fields)
            print("\nSTATUS CODE: " + str(r.status_code))
            print("\ndata: " + str(r.json()))
        with allure.step("Check response status code"):
            assert r.status_code == expected_sc
        with allure.step("Check found issues count"):
            assert r.json()['total'] == expected_count

    @allure.title("Update issue API")
    def test_issue_update(self):
        with allure.step("Sending API request"):
            r = JiraWebService.update_issue_by_id(self.created_issue_ids[0], "Updated: Maxim test issue 1",
                                                  "Medium", "Maksym_Komarenko")
            print("\nSTATUS CODE: " + str(r.status_code))
        with allure.step("Check response status code"):
            assert r.status_code == 204

    @allure.title("Delete issue API")
    def test_issues_delete(self):
        for issue_id in self.created_issue_ids:
            with allure.step("Sending API request"):
                r = JiraWebService.delete_issue_by_id(issue_id)
                print("\nSTATUS CODE: " + str(r.status_code))
            with allure.step("Check response status code"):
                assert r.status_code == 204
