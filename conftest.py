from selenium import webdriver
import pytest
from selene import browser
import tempfile
import shutil

@pytest.fixture(scope='function')
def browser_management():
    # Создаем уникальную временную директорию для user data
    temp_dir = tempfile.mkdtemp()
    
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.add_argument('--headless')
    browser.config.driver_options.add_argument('--window-size=1920,1080')
    browser.config.driver_options.add_argument('--disable-gpu')
    browser.config.driver_options.add_argument('--no-sandbox')
    browser.config.driver_options.add_argument('--disable-dev-shm-usage')
    browser.config.driver_options.add_argument('--headless')  # для Jenkins
    browser.config.driver_options.add_argument('--incognito')  # инкогнито режим
    
    browser.config.timeout = 20

    yield

    browser.quit()
    shutil.rmtree(temp_dir, ignore_errors=True)
