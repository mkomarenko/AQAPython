import pytest
import requests
from Phase2.tests.jira_globals import *
from Phase2.tests.fixtures.json_fixtures import JsonFixtures


class TestJiraIssueSearch:
    url = base_url + '/rest/api/2/search'

    test_data = [
        (JsonFixtures.get_search_issue_json("project = AQAPYTHON AND summary ~ 'Maxim test issue'",
                                            ["id", "key", "summary"]), 200, 34),
        (JsonFixtures.get_search_issue_json("project = AQAPYTHON AND summary ~ 'Maxim test issue 1'",
                                            ["id", "key", "summary"]), 200, 3),
        (JsonFixtures.get_search_issue_json("project = AQAPYTHON AND summary ~ 'Maxim test issue 123'",
                                            ["id", "key", "summary"]), 200, 0),
    ]

    @pytest.mark.parametrize("search_issue_json, expected_sc, expected_count", test_data)
    def test_search_issue(self, search_issue_json, expected_sc, expected_count):
        url = self.url
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=search_issue_json, headers=headers,
                          auth=(login, password))
        print("STATUS CODE: " + str(r.status_code))
        print("data: " + str(r.json()))
        assert r.json()['total'] == expected_count
        assert r.status_code == expected_sc
