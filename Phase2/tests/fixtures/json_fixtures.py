class JsonFixtures:
    @staticmethod
    def get_auth_data():
        return {
            "username": "Maksym_Komarenko",
            "password": "Mk810426@odsu_"
        }

    @staticmethod
    def get_wrong_username():
        return {
            "username": "wrong",
            "password": "Mk810426@odsu_"
        }

    @staticmethod
    def get_wrong_password():
        return {
            "username": "Maksym_Komarenko",
            "password": "wrong"
        }

    @staticmethod
    def get_new_issue_json(summary, description, issue_type, priority):
        return {
            "fields": {
                "project":
                    {
                        "key": "AQAPYTHON"
                    },
                "summary": summary,
                "description": description,
                "issuetype": {
                    "name": issue_type
                    },
                "priority": {
                    "name": priority
                    }
            }
        }

    @staticmethod
    def get_update_issue_json(summary, priority, assignee_name):
        return {
            "fields": {
                "summary": summary,
                "priority": {
                    "name": priority
                },
                "assignee": {
                    "name": assignee_name
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
