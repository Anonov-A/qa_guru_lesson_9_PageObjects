import pytest
from selenium import webdriver
from selene import browser
import tempfile
import shutil

@pytest.fixture(scope='function')
def browser_management():
    # Создаем уникальную временную директорию
    temp_dir = tempfile.mkdtemp()
    
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.add_argument('--window-size=1920,1080')
    browser.config.driver_options.add_argument('--no-sandbox')
    browser.config.driver_options.add_argument('--disable-dev-shm-usage')
    browser.config.driver_options.add_argument('--incognito')
    
    browser.config.timeout = 30

    yield

    try:
        browser.quit()
    except:
        pass
    
    # Очистка временной директории
    shutil.rmtree(temp_dir, ignore_errors=True)
