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
    def get_issue_json(summary):
        return {
            "fields": {
                "project":
                    {
                        "key": "TEST"
                    },
                "summary": summary,
                "description": "Creating of an issue using project keys and issue type names using the REST API",
                "issuetype": {
                    "name": "Bug"
                }
               }
        }
