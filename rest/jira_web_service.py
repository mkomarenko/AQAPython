import requests
from globals.jira_globals import *
from tests.fixtures.json_fixtures import JsonFixtures


class JiraWebService:

    @staticmethod
    def create_new_issue(summary, description, issue_type, priority, assignee):
        url = base_url + '/rest/api/2/issue/'
        headers = {'Content-Type': 'application/json'}
        return requests.post(url,
                             json=JsonFixtures.get_new_issue_json(summary, description, issue_type, priority, assignee),
                             headers=headers,
                             auth=(login, password))

    @staticmethod
    def search_issues_by_jql(jql, fields):
        url = base_url + '/rest/api/2/search'
        headers = {'Content-Type': 'application/json'}
        return requests.post(url, json=JsonFixtures.get_search_issue_json(jql, fields), headers=headers,
                             auth=(login, password))

    @staticmethod
    def update_issue_by_id(issue_id, summary, description, issue_type, priority, assignee):
        url = base_url + '/rest/api/2/issue/' + issue_id
        headers = {'Content-Type': 'application/json'}
        return requests.put(url,
                            json=JsonFixtures.get_update_issue_json(summary, description, issue_type, priority,
                                                                    assignee),
                            headers=headers,
                            auth=(login, password))

    @staticmethod
    def delete_issue_by_id(issue_id):
        url = base_url + '/rest/api/2/issue/' + issue_id
        headers = {'Content-Type': 'application/json'}
        return requests.delete(url, auth=(login, password))

    @staticmethod
    def login(auth_data):
        url = base_url + '/rest/auth/1/session'
        headers = {'Content-Type': 'application/json'}
        return requests.post(url, json=auth_data, headers=headers)
