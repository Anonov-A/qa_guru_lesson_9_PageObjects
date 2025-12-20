from selene import browser, have, be, by
import tempfile
import os
import time


class RegistrationPage:
    def __init__(self):
        # Основные элементы
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.mobile_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.subjects_input = browser.element('#subjectsInput')
        self.upload_picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit_button = browser.element('#submit')

        # Элементы для проверок
        self.modal_window = browser.element('#example-modal-sizes-title-lg')
        self.results_table = browser.all('.table td:nth-child(2)')

    def open(self):
        """Открыть страницу регистрации"""
        browser.open('/automation-practice-form')
        browser.element('body').should(be.visible)
        browser.element('h5').should(have.text('Student Registration Form'))
        return self

    def register(self, user):
        """Выполнить регистрацию пользователя (как в исходном коде)"""

        # Заполнение полей (точно как в вашем исходном тесте)
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)

        # Выбор пола
        browser.element('label[for="gender-radio-1"]').click()

        # Номер телефона
        browser.element('#userNumber').type(user.phone)

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
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            tmp.write(
                b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc\xf8\x0f\x00\x00\x01\x01\x00\x05\x00\x00\x00\x00IEND\xaeB`\x82')
            temp_file = tmp.name

        browser.element('#uploadPicture').set_value(temp_file)
        picture_filename = os.path.basename(temp_file)

        # Адрес
        browser.element('#currentAddress').type(user.address)

        # Штат и город
        browser.element('[id="state"]').click()
        browser.element('#react-select-3-option-0').click()  # NCR

        browser.element('#city').click()
        browser.element('#react-select-4-option-0').click()  # Delhi

        # Отправка формы
        browser.element('#submit').click()

        return picture_filename

    def should_have_registered(self, user, picture_filename=None):
        """Проверить успешность регистрации"""

        # Проверяем заголовок модального окна
        self.modal_window.should(have.text('Thanks for submitting the form'))

        # Формируем ожидаемые значения (точно как в вашем тесте)
        expected_values = [
            'Алексей Антонов',
            'antonov@example.com',
            'Male',
            '7951777777',
            '27 July,1900',
            'Maths',
            'Music',
            picture_filename,
            'Puskina, Kolotuskina, 123456789',
            'NCR Delhi'
        ]

        # Проверяем таблицу
        self.results_table.should(have.exact_texts(*expected_values))

        return self