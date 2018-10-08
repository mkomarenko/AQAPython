from globals.jira_globals import project


class JsonFixtures:
    @staticmethod
    def get_auth_data(login, password):
        return {
            "username": login,
            "password": password
        }

    @staticmethod
    def get_new_issue_json(summary, description, issue_type, priority, assignee):
        return {
            "fields": {
                "project":
                    {
                        "key": project
                    },
                "summary": summary,
                "description": description,
                "issuetype": {
                    "name": issue_type
                },
                "priority": {
                    "name": priority
                },
                "assignee": {
                    "name": assignee
                }
            }
        }

    @staticmethod
    def get_update_issue_json(summary, description, issue_type, priority, assignee):
        return {
            "fields": {
                "summary": summary,
                "description": description,
                "issuetype": {
                    "name": issue_type
                },
                "priority": {
                    "name": priority
                },
                "assignee": {
                    "name": assignee
                }
            }
        }

    @staticmethod
    def get_search_issue_json(jql, fields):
        return {
            "jql": jql,
            "startAt": 0,
            "fields": fields
        }
