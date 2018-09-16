import pytest


@pytest.fixture(scope="class")
def driver_init(request):
    from selenium import webdriver
    web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    yield
    web_driver.close()
