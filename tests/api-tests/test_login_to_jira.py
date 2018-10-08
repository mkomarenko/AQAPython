import allure
import pytest
import requests
from globals.jira_globals import *
from rest.jira_web_service import JiraWebService
from tests.fixtures.json_fixtures import JsonFixtures


@pytest.mark.api_test
class TestLogin:

    test_data = [
        (JsonFixtures.get_auth_data(login, password), 200),
        (JsonFixtures.get_auth_data("wrong", password), 401),
        (JsonFixtures.get_auth_data(login, "wrong"), 401),
    ]

    jira_url = base_url + '/rest/auth/1/session'

    @allure.title("Login to Jira API")
    @pytest.mark.parametrize("auth_data, expected", test_data)
    def test_login_to_jira(self, auth_data, expected):
            with allure.step("Calling login method"):
                r = JiraWebService.login(auth_data)
                print("\nSTATUS CODE: " + str(r.status_code))
                print("\ndata: " + str(r.json()) + "\n")
            with allure.step("Check response status code"):
                assert r.status_code == expected
