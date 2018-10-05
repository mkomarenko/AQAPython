import allure
import pytest

from globals.jira_globals import *


@pytest.mark.ui_test
@pytest.mark.incremental
class TestLoginUI:

    @allure.title("Login to Jira UI with incorrect username")
    def test_login_incorrect_username(self, get_login_page, get_driver):
        with allure.step("Open login page"):
            get_login_page.open()
        with allure.step("Check that login page opened"):
            assert get_login_page.at_page()
        with allure.step("Call login method"):
            get_login_page.login("wrong", password)
        with allure.step("Check that correct error is displayed"):
            assert get_login_page.is_username_error_displayed()
            assert "Sorry, your username and password are incorrect" in get_login_page.get_username_error_text()
            allure.attach(get_driver.get_screenshot_as_png(),
                          name="test_login_incorrect_username",
                          attachment_type=allure.attachment_type.PNG)

    @allure.title("Login to Jira UI with incorrect password")
    def test_login_incorrect_password(self, get_login_page, get_driver):
        with allure.step("Open login page"):
            get_login_page.open()
        with allure.step("Check that login page opened"):
            assert get_login_page.at_page()
        with allure.step("Call login method"):
            get_login_page.login(login, "wrong")
        with allure.step("Check that correct error is displayed"):
            assert get_login_page.is_username_error_displayed()
            assert "Sorry, your username and password are incorrect" in get_login_page.get_username_error_text()
            allure.attach(get_driver.get_screenshot_as_png(),
                          name="test_login_incorrect_password",
                          attachment_type=allure.attachment_type.PNG)

    @allure.title("Login to Jira UI")
    def test_login_correct_creds(self, get_login_page, get_main_page, get_driver):
        with allure.step("Open login page"):
            get_login_page.open()
        with allure.step("Check that login page opened"):
            assert get_login_page.at_page()
        with allure.step("Call login method"):
            get_login_page.login(login, password)
        with allure.step("Check that main page opened"):
            assert get_main_page.at_page()
            allure.attach(get_driver.get_screenshot_as_png(),
                          name="test_login_correct_creds",
                          attachment_type=allure.attachment_type.PNG)

    @allure.title("Logout from Jira UI")
    def test_logout(self, get_main_page, get_login_page, get_driver):
        with allure.step("Call logout method"):
            get_main_page.logout()
        with allure.step("Open login page"):
            get_login_page.open()
        with allure.step("Check that login page opened"):
            assert get_login_page.at_page()
            allure.attach(get_driver.get_screenshot_as_png(),
                          name="test_logout",
                          attachment_type=allure.attachment_type.PNG)
