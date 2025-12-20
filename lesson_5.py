import os
import tempfile
import pytest
from selene import browser, have, be, query
from selenium import webdriver




@pytest.fixture(scope='function')
def config_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver_options = webdriver.ChromeOptions()


    browser.config.driver_options.add_argument('--window-size=1920,1080')
    browser.config.timeout = 20  # Увеличить timeout
    yield
    browser.quit()


def test_registration_form(config_browser):
    browser.open('/automation-practice-form')

    # Ждем загрузки страницы
    browser.element('body').should(be.visible)
    browser.element('h5').should(have.text('Student Registration Form'))

    # Создаем временный файл
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
        tmp.write(
            b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc\xf8\x0f\x00\x00\x01\x01\x00\x05\x00\x00\x00\x00IEND\xaeB`\x82')
        temp_file = tmp.name

    # Заполнение полей
    browser.element('#firstName').type('Алексей')
    browser.element('#lastName').type('Антонов')
    browser.element('#userEmail').type('antonov@example.com')

    # Выбор пола
    browser.element('label[for="gender-radio-1"]').click()

    #номер телефона
    browser.element('#userNumber').type('7951777777')

    # Дата рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="6"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1900"]').click()
    browser.element('.react-datepicker__day--027:not(.react-datepicker__day--outside-month)').click()

    # Предметы
    browser.element('#subjectsInput').type('Maths').press_enter()

    # Хобби - JavaScript клик
    label = browser.element('label[for="hobbies-checkbox-3"]').locate()
    browser.execute_script("arguments[0].click();", label)

    # Загрузка файла
    browser.element('#uploadPicture').set_value(temp_file)

    # Адрес
    browser.element('#currentAddress').type('Puskina, Kolotuskina, 123456789')

    # Штат и город
    browser.element('[id="state"]').click()
    browser.element('#react-select-3-option-0').click()  # NCR

    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()  # Delhi

    # Отправка формы
    browser.element('#submit').click()

    # Проверка результата
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    # Проверка таблицы - отладочная информация
    print("=== DEBUG: Checking table values ===")
    cells = browser.all('.table td:nth-child(2)')
    actual_texts = []
    for i, cell in enumerate(cells):
        # используем query.text
        text = cell.get(query.text)
        actual_texts.append(text)
        print(f"Row {i}: '{text}'")

    # Проверяем, есть ли 'Music' в таблице
    if 'Music' in actual_texts:
        print("Great! 'Music' is selected!")
    else:
        print("Warning: 'Music' not found in table")

    # Проверка таблицы
    browser.all('.table td:nth-child(2)').should(have.exact_texts(
        'Алексей Антонов',
        'antonov@example.com',
        'Male',
        '7951777777',
        '27 July,1900',
        'Maths',
        'Music',  # Если не выбралось, замените на ''
        os.path.basename(temp_file),
        'Puskina, Kolotuskina, 123456789',
        'NCR Delhi'
    ))

    # Очистка
    os.unlink(temp_file)