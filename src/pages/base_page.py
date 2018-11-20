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

    def take_screenshot(self, name):
        import allure
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=name,
                      attachment_type=allure.attachment_type.PNG)
