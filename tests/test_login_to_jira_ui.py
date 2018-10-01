from globals.jira_globals import *


class TestJiraLoginUI:

    def test_login_incorrect_username(self, get_login_page):
        login_page = get_login_page
        login_page.open()
        assert login_page.at_page()
        login_page.login("wrong", password)
        assert login_page.is_username_error_displayed()
        assert "Sorry, your username and password are incorrect" in login_page.get_username_error_text()

    def test_login_incorrect_password(self, get_login_page):
        login_page = get_login_page
        login_page.open()
        assert login_page.at_page()
        login_page.login(login, "wrong")
        assert login_page.is_username_error_displayed()
        assert "Sorry, your username and password are incorrect" in login_page.get_username_error_text()

    def test_login_correct_creds(self, get_login_page, get_main_page):
        main_page = get_main_page
        login_page = get_login_page
        login_page.open()
        assert login_page.at_page()
        login_page.login(login, password)
        assert main_page.at_page()

    def test_logout(self, get_main_page, get_login_page):
        main_page = get_main_page
        main_page.logout()
        login_page = get_login_page
        login_page.open()
        assert login_page.at_page()
