import pytest
import requests
from Phase2.tests.jira_globals import *
from Phase2.tests.fixtures.json_fixtures import JsonFixtures


class TestJiraIssueCrud:
    jira_url = base_url + '/rest/api/2/issue/'

    def test_issue_create(self):
        headers = {'Content-Type': 'application/json'}
        r = requests.post(self.jira_url, json=JsonFixtures.get_issue_json('Maxim 07/09'), headers=headers,
                          auth=(login, password))
        print("STATUS CODE: " + str(r.status_code))
        assert r.status_code == 201
