from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from tests.base_test import BaseTest


class TestJiraLoginUI(BaseTest):
    def test_login_page(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get("http://jira.hillel.it:8080")
        wait.until(EC.visibility_of_element_located((By.ID, "login-form-username")))
