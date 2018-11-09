import allure
import pytest

from globals.jira_globals import *


@allure.step("Getting web driver")
@pytest.fixture(scope="session")
def browser():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    with webdriver.Chrome(ChromeDriverManager().install()) as browser:
        yield browser


@allure.step("Login to Jira before tests started and logout after tests finished")
@pytest.fixture(scope="function")
def login_to_jira(browser):
    from src.pages.login_page import LoginPage
    login_page = LoginPage(browser)
    with allure.step("Open login page"):
        login_page.open()
    with allure.step("Login to JIRA"):
        main_page = login_page.login(login, password)
    yield
    with allure.step("Logout from JIRA"):
        main_page.logout()


@pytest.fixture(scope="class")
def jira_test_data():
    from rest.jira_web_service import JiraWebService

    test_data = (("Maxim search issue 1", "Maxim test issue", "Bug", "Low", ""),
                 ("Maxim search issue 2", "Maxim test issue", "User Story", "High", ""),
                 ("Maxim search issue 3", "Maxim test issue", "Test", "Medium", ""),
                 ("Maxim search issue 4", "Maxim test issue", "Task", "Lowest", ""),
                 ("Maxim search issue 5", "Maxim test issue", "Story", "Highest", ""))
    issue_ids = []
    with allure.step("Setup issues"):
        for record in test_data:
            r = JiraWebService.create_new_issue(*record)
            issue_ids.append(r.json()['id'])
    yield
    with allure.step("Cleanup issues"):
        r = JiraWebService.search_issues_by_jql(
            "reporter = currentuser() AND summary ~ 'Maxim' AND project = " + project,
            ["id"])
        for issue in r.json()['issues']:
            JiraWebService.delete_issue_by_id(issue.get('id'))


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item
    outcome = yield
    rep = outcome.get_result()
    if browser is not None:
        if rep.when in 'call' and rep.failed:
            allure.attach(browser.get_screenshot_as_png(),
                          name=item._pyfuncitem.name,
                          attachment_type=allure.attachment_type.PNG)


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" % previousfailed.name)
