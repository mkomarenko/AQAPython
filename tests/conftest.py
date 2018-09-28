import pytest
from selenium.webdriver.support.wait import WebDriverWait
from globals.jira_globals import *

@pytest.fixture(scope="module")
def driver_init(request):
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    web_driver_wait = WebDriverWait(web_driver, 10)
    request.cls.driver = web_driver
    request.cls.wait = web_driver_wait
    yield
    web_driver.close()


@pytest.fixture(scope="class")
def jira_cleanup():
    from rest.jira_web_service import JiraWebService
    yield
    r = JiraWebService.search_issues_by_jql(
        "project = " + project + " AND reporter = " + login,
        ["id"])
    for issue in r.json()['issues']:
        JiraWebService.delete_issue_by_id(issue.get('id'))

