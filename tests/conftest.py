import allure
import pytest

from globals.jira_globals import *


@allure.step("Getting web driver")
@pytest.fixture(scope="function")
def browser():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.microsoft import IEDriverManager

    br = pytest.config.getoption("-B")
    if br.lower() == "firefox":
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif br.lower() == "chrome":
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif br.lower() == "ie":
        browser = webdriver.Ie(executable_path=IEDriverManager().install())
    else:
        raise Exception(
            '{} is unknown browser. Please specify one of the following: firefox(default), chrome or ie'.format(br))
    yield browser
    browser.close()
    browser.quit()


@allure.step("Login to Jira before tests started and logout after tests finished")
@pytest.fixture(scope="function")
def login_to_jira(request, browser):
    from src.pages.login_page import LoginPage
    from src.pages.main_page import MainPage
    login_page = LoginPage(browser)
    main_page = MainPage(browser)

    with allure.step("Open login page"):
        login_page.open()
    with allure.step("Login to JIRA"):
        login_page.login(login, password)

    def take_screenshot():
        with allure.step("Taking screenshot"):
            browser.execute_script("document.body.bgColor = 'white';")
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

    request.addfinalizer(take_screenshot)

    with allure.step("Wait until main page is loaded"):
        main_page.wait_until_loaded()

    yield main_page

    with allure.step("Logout from JIRA"):
        main_page.logout()


@pytest.fixture(scope="function")
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
        for issue_id in issue_ids:
            JiraWebService.delete_issue_by_id(issue_id)


@pytest.fixture(scope="function")
def jira_cleanup(request):
    from rest.jira_web_service import JiraWebService
    summary_contains = "Maxim"
    yield
    r = JiraWebService.search_issues_by_jql(
        "reporter = currentuser() AND summary ~ '" + summary_contains + "' AND project = " + project,
        ["id"])
    for issue in r.json()['issues']:
        JiraWebService.delete_issue_by_id(issue.get('id'))


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" % previousfailed.name)


def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     dest="browser",
                     default="firefox",
                     help="Browser. Valid options are firefox, ie and chrome")
