import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selene import browser
import tempfile
import shutil
import time
import subprocess

@pytest.fixture(scope='function')
def browser_management():
    # Создаем уникальную временную директорию
    temp_dir = tempfile.mkdtemp()
    
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument(f'--user-data-dir={temp_dir}')
    
    # Используем webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 60
    browser.config.page_load_timeout = 120

    yield

    # Закрываем драйвер
    try:
        driver.quit()
    except Exception as e:
        print(f"Error during driver quit: {e}")
        # Принудительно убиваем процессы
        subprocess.run(['pkill', '-9', '-f', 'chrome'], capture_output=True)
        subprocess.run(['pkill', '-9', '-f', 'chromedriver'], capture_output=True)
    
    # Очищаем временную директорию
    shutil.rmtree(temp_dir, ignore_errors=True)
    
    # Задержка между тестами
    time.sleep(1)
