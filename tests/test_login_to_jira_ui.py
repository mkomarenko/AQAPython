from globals.jira_globals import *
from src.pages.jira_login_page import JiraLoginPage
from src.pages.jira_main_page import JiraMainPage
from tests.base_test import BaseTest


class TestJiraLoginUI(BaseTest):

    def init_login_page(self):
        self.login_page = JiraLoginPage(self.driver, self.wait)

    def init_main_page(self):
        self.main_page = JiraMainPage(self.driver, self.wait)

    def test_login_incorrect_username(self):
        self.init_login_page()
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.login("wrong", password)
        assert self.login_page.is_username_error_displayed()

    def test_login_incorrect_password(self):
        self.init_login_page()
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.login(login, "wrong")
        assert self.login_page.is_username_error_displayed()

    def test_login_correct_creds(self):
        self.init_login_page()
        self.init_main_page()
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.login(login, password)
        assert self.main_page.at_page()
