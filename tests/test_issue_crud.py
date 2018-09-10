import pytest
from tests.jira_web_service import *


class TestJiraIssueCRUD:
    created_issues = []

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

    @pytest.mark.parametrize("summary, description, issue_type, priority, assignee, expected_sc, expected_text",
                             create_test_data)
    def test_issue_create(self, summary, description, issue_type, priority, assignee, expected_sc, expected_text):
        r = JiraWebService.create_new_issue(summary, description, issue_type, priority, assignee)
        print("STATUS CODE: " + str(r.status_code))
        print("data: " + str(r.json()))
        if r.status_code == 201:
            self.created_issues.append(r.json()['id'])
        assert expected_text in str(r.json())
        assert r.status_code == expected_sc

    @pytest.mark.parametrize("jql, fields, expected_sc, expected_count", search_test_data)
    def test_search_issue(self, jql, fields, expected_sc, expected_count):
        r = JiraWebService.search_issues_by_jql(jql, fields)
        print("STATUS CODE: " + str(r.status_code))
        print("data: " + str(r.json()))
        assert r.json()['total'] >= expected_count
        assert r.status_code == expected_sc

    def test_issue_update(self):
        r = JiraWebService.update_issue_by_id(self.created_issues[0], "Updated: Maxim test issue 1",
                                              "Medium", "Maksym_Komarenko")
        print("STATUS CODE: " + str(r.status_code))
        assert r.status_code == 204
        # print(self.created_issues)

    def test_issues_delete(self):
        r = JiraWebService.search_issues_by_jql(
            "project = AQAPYTHON AND reporter = Maksym_Komarenko",
            ["id"])
        for issue in r.json()['issues']:
            r = JiraWebService.delete_issue_by_id(issue.get('id'))
            assert r.status_code == 204
