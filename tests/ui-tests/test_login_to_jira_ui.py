import allure
import pytest

from globals.jira_globals import *
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage


@pytest.mark.ui_test
@pytest.mark.incremental
@pytest.mark.usefixtures("take_screenshot")
class TestLoginUI:

    @allure.title("Login to Jira UI")
    def test_login_correct_creds(self, browser):
        login_page = LoginPage(browser)
        with allure.step("Open login page"):
            login_page.open()
        with allure.step("Check that login page opened"):
            assert login_page.at_page()
        with allure.step("Call login method"):
            main_page = login_page.login(login, password)
            allure.attach(browser.get_screenshot_as_png(),
                          name="test_login_correct_creds1",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Check that main page opened"):
            assert main_page.at_page()
            allure.attach(browser.get_screenshot_as_png(),
                          name="test_login_correct_creds2",
                          attachment_type=allure.attachment_type.PNG)

    @allure.title("Logout from Jira UI")
    def test_logout(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        with allure.step("Call logout method"):
            logout_page = main_page.logout()
        with allure.step("Cheсk that logout page appears"):
            assert logout_page.at_page()
        with allure.step("Open login page"):
            login_page.open()
        with allure.step("Check that login page opened"):
            assert login_page.at_page()
            allure.attach(browser.get_screenshot_as_png(),
                          name="test_logout",
                          attachment_type=allure.attachment_type.PNG)

    @allure.title("Login to Jira UI with incorrect username")
    def test_login_incorrect_username(self, browser):
        login_page = LoginPage(browser)
        with allure.step("Open login page"):
            login_page.open()
        with allure.step("Check that login page opened"):
            assert login_page.at_page()
            allure.attach(browser.get_screenshot_as_png(),
                          name="test_login_incorrect_username1",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Call login method"):
            login_page.login("wrong", password)
        with allure.step("Check that correct error is displayed"):
            assert login_page.username_error_text("Sorry, your username and password are incorrect")
            allure.attach(browser.get_screenshot_as_png(),
                          name="test_login_incorrect_username2",
                          attachment_type=allure.attachment_type.PNG)

    @allure.title("Login to Jira UI with incorrect password")
    def test_login_incorrect_password(self, browser):
        login_page = LoginPage(browser)
        with allure.step("Open login page"):
            login_page.open()
        with allure.step("Check that login page opened"):
            assert login_page.at_page()
        with allure.step("Call login method"):
            login_page.login(login, "wrong")
        with allure.step("Check that correct error is displayed"):
            assert login_page.username_error_text("Sorry, your username and password are incorrect")
            allure.attach(browser.get_screenshot_as_png(),
                          name="test_login_incorrect_password",
                          attachment_type=allure.attachment_type.PNG)


