import requests
from Phase2.tests.fixtures.json_fixtures import JsonFixtures


class TestJiraLogin:

    def test_login_to_jira(self):

        jira_url='http://jira.hillel.it:8080/rest/auth/1/session'

        auth_data=JsonFixtures.get_auth_data()

        headers = {'Content-Type': 'application/json'}
        r = requests.post(jira_url, json=auth_data, headers=headers)
        print("STATUS CODE: " + str(r.status_code))
        assert r.status_code is 200