import pytest
import requests
from Phase2.tests.jira_globals import *
from Phase2.tests.fixtures.json_fixtures import JsonFixtures


class TestJiraIssueCreate:
    jira_url = base_url + '/rest/api/2/issue/'
    test_data = [
        (JsonFixtures.get_new_issue_json("Maxim test issue", "Maxim test issue", "Bug"), 201, jira_url),
        (JsonFixtures.get_new_issue_json("", "Maxim test issue", "Bug"), 400,
         'You must specify a summary of the issue.'),
        (JsonFixtures.get_new_issue_json(
            "Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test Maxim test 123",
            "Maxim test issue", "Bug"), 400, 'Summary must be less than 255 characters.'),
    ]

    @pytest.mark.parametrize("issue_json, expected_rc, expected_text", test_data)
    def test_issue_create(self, issue_json, expected_rc, expected_text):
        url = self.jira_url
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=issue_json, headers=headers,
                          auth=(login, password))
        print("STATUS CODE: " + str(r.status_code))
        print("data: " + str(r.json()))
        # if r.status_code == 201:
        # self.issue_id = r.json()['id']
        assert expected_text in str(r.json())
        assert r.status_code == expected_rc
