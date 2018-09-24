from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class JiraMainPage:
    URL = "http://jira.hillel.it:8080/secure/Dashboard.jspa"
    CREATE_BUTTON = (By.ID, "create_link")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open(self):
        self.driver.get(self.URL)
        return self

    def at_page(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "create_link"))).is_displayed()
