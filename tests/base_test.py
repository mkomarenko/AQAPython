from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:
    def setup_class(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 30)

    def teardown_class(self):
        self.driver.close()
        self.driver.quit()
