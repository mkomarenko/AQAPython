import pytest
import requests
from tests.jira_globals import *
from tests.fixtures.json_fixtures import JsonFixtures


class TestJiraLogin:

    test_data = [
        (JsonFixtures.get_auth_data(), 200),
        (JsonFixtures.get_wrong_username(), 401),
        (JsonFixtures.get_wrong_password(), 401),
    ]

    jira_url = base_url + '/rest/auth/1/session'

    @pytest.mark.parametrize("auth_data, expected", test_data)
    def test_login_to_jira(self, auth_data, expected):
        headers = {'Content-Type': 'application/json'}
        r = requests.post(self.jira_url, json=auth_data, headers=headers)
        print("STATUS CODE: " + str(r.status_code))
        assert r.status_code == expected
