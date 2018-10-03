import allure
import pytest

from globals.jira_globals import *


@pytest.mark.ui_test
@pytest.mark.incremental
class TestLoginUI:

    @allure.title("Login to Jira UI negative")
    def test_login_incorrect_username(self, get_login_page):
        with allure.step("Opening login page"):
            login_page = get_login_page
            login_page.open()
            assert login_page.at_page()
        with allure.step("Trying to login with wrong username"):
            login_page.login("wrong", password)
            assert login_page.is_username_error_displayed()
            assert "Sorry, your username and password are incorrect" in login_page.get_username_error_text()

    @allure.title("Login to Jira UI negative")
    def test_login_incorrect_password(self, get_login_page):
        with allure.step("Opening login page"):
            login_page = get_login_page
            login_page.open()
            assert login_page.at_page()
        with allure.step("Trying to login with wrong password"):
            login_page.login(login, "wrong")
            assert login_page.is_username_error_displayed()
            assert "Sorry, your username and password are incorrect" in login_page.get_username_error_text()

    @allure.title("Login to Jira UI")
    def test_login_correct_creds(self, get_login_page, get_main_page):
        with allure.step("Opening login page"):
            login_page = get_login_page
            login_page.open()
            assert login_page.at_page()
        with allure.step("Login with correct credentials"):
            login_page.login(login, password)
            main_page = get_main_page
            assert main_page.at_page()

    @allure.title("Logout from Jira UI")
    def test_logout(self, get_main_page, get_login_page):
        with allure.step("Logging out"):
            main_page = get_main_page
            main_page.logout()
        with allure.step("Opening login page"):
            login_page = get_login_page
            login_page.open()
            assert login_page.at_page()
