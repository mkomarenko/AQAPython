import pytest

from globals.jira_globals import *


@pytest.fixture(scope="session")
def get_driver():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    yield web_driver
    web_driver.close()


@pytest.fixture(scope="class")
def get_login_page(get_driver):
    from src.pages.login_page import LoginPage
    return LoginPage(get_driver)


@pytest.fixture(scope="class")
def get_main_page(get_driver):
    from src.pages.main_page import MainPage
    return MainPage(get_driver)


@pytest.fixture(scope="class")
def get_new_issue_page(get_driver):
    from src.pages.new_issue_page import NewIssuePage
    return NewIssuePage(get_driver)


@pytest.fixture(scope="class")
def get_search_page(get_driver):
    from src.pages.search_page import SearchPage
    return SearchPage(get_driver)


@pytest.fixture(scope="class")
def get_edit_issue_page(get_driver):
    from src.pages.edit_issue_page import EditIssuePage
    return EditIssuePage(get_driver)


@pytest.fixture(scope="class")
def get_issue_summary_page(get_driver):
    from src.pages.issue_summary_page import IssueSummaryPage
    return IssueSummaryPage(get_driver)


@pytest.fixture(scope="class")
def login_logout(get_login_page, get_main_page):
    login_page = get_login_page
    login_page.open()
    login_page.login(login, password)
    main_page = get_main_page
    main_page.wait_until_page_is_loaded(15)
    yield
    main_page.logout()


@pytest.fixture(scope="class")
def jira_cleanup():
    from rest.jira_web_service import JiraWebService
    yield
    r = JiraWebService.search_issues_by_jql(
        "reporter = " + login,
        ["id"])
    for issue in r.json()['issues']:
        JiraWebService.delete_issue_by_id(issue.get('id'))


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" %previousfailed.name)

