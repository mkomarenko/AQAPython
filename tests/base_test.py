from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:
    driver_executable_path = None

    def init_diver_executable(self):
        if BaseTest.driver_executable_path is None:
            BaseTest.driver_executable_path = ChromeDriverManager().install()

    def setup_class(self):
        self.init_diver_executable(self)
        self.driver = webdriver.Chrome(BaseTest.driver_executable_path)
        self.wait = WebDriverWait(self.driver, 30)

    def teardown_class(self):
        self.driver.close()
        self.driver.quit()
