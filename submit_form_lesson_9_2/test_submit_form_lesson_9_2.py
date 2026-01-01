import pytest
from datetime import date
from selene import browser
from selenium import webdriver
from submit_form_lesson_9_2.models.models import User
from submit_form_lesson_9_2.pages.pages import RegistrationPage


@pytest.fixture(scope='function')
def browser_management():
    from selenium import webdriver
    from selene import browser
    import time
    
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--incognito')
    
    # Увеличиваем таймауты
    browser.config.driver_options = options
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 60  # Увеличиваем таймаут
    browser.config.page_load_timeout = 120

    yield

    # Даем браузеру больше времени на закрытие
    try:
        browser.quit()
    except Exception as e:
        print(f"Error during browser quit: {e}")
        # Пытаемся убить процесс принудительно
        import subprocess
        subprocess.run(['pkill', '-f', 'chrome'], capture_output=True)
        subprocess.run(['pkill', '-f', 'chromedriver'], capture_output=True)
    
    # Добавляем небольшую задержку между тестами
    time.sleep(2)



def test_registration_alexey(browser_management):

    user = User(
        first_name='Алексей',
        last_name='Антонов',
        email='antonov@example.com',
        gender='Male',
        phone='7951777777',
        birth_date=date(1900, 7, 27),
        subjects=['Maths'],
        hobbies=['Music'],
        address='Puskina, Kolotuskina, 123456789',
        state='NCR',
        city='Delhi'
    )

    registration_page = RegistrationPage()

    picture_filename = registration_page.open().register(user)
    registration_page.should_have_registered(user, picture_filename)
