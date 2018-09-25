from globals.jira_globals import *
from src.pages.login_page import JiraLoginPage
from src.pages.main_page import JiraMainPage
from tests.base_test import BaseTest


class TestJiraLoginUI(BaseTest):

    def setup_method(self):
        self.login_page = JiraLoginPage(self.driver, self.wait)
        self.main_page = JiraMainPage(self.driver, self.wait)

    def test_login_incorrect_username(self):
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.login("wrong", password)
        assert self.login_page.is_username_error_displayed()
        assert "Sorry, your username and password are incorrect" in self.login_page.get_username_error_text()

    def test_login_incorrect_password(self):
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.login(login, "wrong")
        assert self.login_page.is_username_error_displayed()
        assert "Sorry, your username and password are incorrect" in self.login_page.get_username_error_text()

    def test_login_correct_creds(self):
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.login(login, password)
        assert self.main_page.at_page()
