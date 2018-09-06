import pytest
import requests
from Phase2.tests.fixtures.json_fixtures import JsonFixtures


class TestJiraLogin:

    testdata = [
        (JsonFixtures.get_auth_data(), 200),
    ]

    @pytest.mark.parametrize("auth_data, expected", testdata)
    def test_login_to_jira(self, auth_data, expected):

        jira_url='http://jira.hillel.it:8080/rest/auth/1/session'

        headers = {'Content-Type': 'application/json'}
        r = requests.post(jira_url, json=auth_data, headers=headers)
        print("STATUS CODE: " + str(r.status_code))
        assert r.status_code is expected
