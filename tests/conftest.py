import pytest
from selenium.webdriver.support.wait import WebDriverWait


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
