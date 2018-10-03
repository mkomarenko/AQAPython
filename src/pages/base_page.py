import time
from abc import abstractmethod

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @abstractmethod
    def at_page(self):
        pass

    def wait_until_page_is_loaded(self, timeoutsec):
        check_interval = 1
        wait_time = 0
        while not self.at_page() and wait_time < timeoutsec:
            time.sleep(check_interval)
            wait_time += check_interval

