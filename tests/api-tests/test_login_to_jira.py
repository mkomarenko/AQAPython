import allure
import pytest
import requests
from globals.jira_globals import *
from tests.fixtures.json_fixtures import JsonFixtures


@pytest.mark.api_test
class TestLogin:

    test_data = [
        (JsonFixtures.get_auth_data(), 200),
        (JsonFixtures.get_wrong_username(), 401),
        (JsonFixtures.get_wrong_password(), 401),
    ]

    jira_url = base_url + '/rest/auth/1/session'

    @allure.title("Login to Jira API")
    @pytest.mark.parametrize("auth_data, expected", test_data)
    def test_login_to_jira(self, auth_data, expected):
            headers = {'Content-Type': 'application/json'}
            with allure.step("Sending POST request"):
                r = requests.post(self.jira_url, json=auth_data, headers=headers)
                print("\nSTATUS CODE: " + str(r.status_code))
                print("\ndata: " + str(r.json()) + "\n")
            with allure.step("Check response status code"):
                assert r.status_code == expected