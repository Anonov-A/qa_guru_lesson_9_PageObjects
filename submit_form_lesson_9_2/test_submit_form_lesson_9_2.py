import os
import tempfile
import pytest
from datetime import date
from selene import browser
from selenium import webdriver
from models import User
from pages import RegistrationPage


@pytest.fixture(scope='function')
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.add_argument('--window-size=1920,1080')
    browser.config.timeout = 30

    yield

    browser.quit()


def test_registration_alexey(browser_management):
    """Тест с данными Алексея"""

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

    # Очистка временного файла
    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, picture_filename)
    if os.path.exists(temp_file_path):
        os.unlink(temp_file_path)