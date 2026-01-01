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
    
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.add_argument('--window-size=1920,1080')
    browser.config.driver_options.add_argument('--no-sandbox')
    browser.config.driver_options.add_argument('--disable-dev-shm-usage')
    browser.config.driver_options.add_argument('--headless')
    browser.config.driver_options.add_argument('--incognito')  # или --no-user-data-dir
    browser.config.timeout = 30

    yield

    browser.quit()



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
