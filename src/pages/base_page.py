import time
from abc import abstractmethod

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    @abstractmethod
    def wait_until_loaded(self):
        pass

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

