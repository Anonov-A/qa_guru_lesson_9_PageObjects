# conftest.py
import pytest
from selenium import webdriver
from selene import browser
import tempfile
import shutil

@pytest.fixture(scope='function')
def browser_management():
    
    temp_dir = tempfile.mkdtemp()
    
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--incognito') 
    options.add_argument(f'--user-data-dir={temp_dir}')
    
    browser.config.driver_options = options
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 20

    yield

    browser.quit()
    
    # Очистка временной директории
    shutil.rmtree(temp_dir, ignore_errors=True)
