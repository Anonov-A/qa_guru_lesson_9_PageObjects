import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function')
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.add_argument('--window-size=1920,1080')
    browser.config.timeout = 20

    yield

    browser.quit()