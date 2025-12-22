from selene import browser, have, be, query, by
import tempfile
import os
import time


class RegistrationPage:
    def __init__(self):
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
        self.modal_window = browser.element('#example-modal-sizes-title-lg')
        self.info_about_the_registered_user = browser.all('.table td:nth-child(2)')

    def open(self):
        browser.open('/automation-practice-form')
        browser.element('body').should(be.visible)
        browser.element('h5').should(have.text('Student Registration Form'))
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def fill_gender(self, gender='Male'):
        """Выбор пола с параметром"""
        if gender.lower() == 'male':
            browser.element('label[for="gender-radio-1"]').click()
        elif gender.lower() == 'female':
            browser.element('label[for="gender-radio-2"]').click()
        else:
            browser.element('label[for="gender-radio-3"]').click()
        return self

    def fill_mobile_number(self, value):
        self.mobile_number.type(value)
        return self

    def fill_date(self, date_str='27 July,1900'):
        """Выбор даты рождения с параметром в формате '27 July,1900'"""
        parts = date_str.replace(',', ' ').split()
        day = parts[0]
        month = parts[1]
        year = parts[2]

        # Месяцы в числовом формате для select
        month_map = {
            'January': '0', 'February': '1', 'March': '2', 'April': '3',
            'May': '4', 'June': '5', 'July': '6', 'August': '7',
            'September': '8', 'October': '9', 'November': '10', 'December': '11'
        }

        month_num = month_map.get(month, '6')  # По умолчанию July

        self.date_of_birth.click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'option[value="{month_num}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'option[value="{year}"]').click()

        day_formatted = f'0{day}' if len(day) == 1 else day
        browser.element(f'.react-datepicker__day--0{day_formatted}:not(.react-datepicker__day--outside-month)').click()

        return self

    def select_subjects(self, subject):
        self.subjects_input.type(subject).press_enter()
        return self

    def select_hobbies(self, hobby='Music'):
        """Выбор хобби с параметром"""
        hobby_map = {
            'Sports': 'hobbies-checkbox-1',
            'Reading': 'hobbies-checkbox-2',
            'Music': 'hobbies-checkbox-3'
        }

        checkbox_id = hobby_map.get(hobby, 'hobbies-checkbox-3')
        label = browser.element(f'label[for="{checkbox_id}"]').locate()
        browser.execute_script("arguments[0].click();", label)
        return self

    def load_picture(self, filename=None):
        """Загрузка файла с возможностью указания имени"""
        if not filename:
            # Создаем временный файл
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
                tmp.write(
                    b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc\xf8\x0f\x00\x00\x01\x01\x00\x05\x00\x00\x00\x00IEND\xaeB`\x82')
                filename = tmp.name

        self.upload_picture.set_value(filename)
        return os.path.basename(filename)

    def fill_adress(self, address):
        self.current_address.type(address)
        return self

    def choice_state(self, state='NCR'):
        """Выбор штата с параметром"""
        self.state.click()
        time.sleep(1)


        state_map = {
            'NCR': '#react-select-3-option-0',
            'Uttar Pradesh': '#react-select-3-option-1',
            'Haryana': '#react-select-3-option-2',
            'Rajasthan': '#react-select-3-option-3'
        }

        selector = state_map.get(state, '#react-select-3-option-0')
        browser.element(selector).click()
        return self

    def choice_city(self, city='Delhi'):
        """Выбор города с параметром"""
        self.city.click()
        time.sleep(1)

        city_map = {
            'Delhi': '#react-select-4-option-0',
            'Gurgaon': '#react-select-4-option-1',
            'Noida': '#react-select-4-option-2',
            'Agra': '#react-select-4-option-0',
            'Lucknow': '#react-select-4-option-1',
            'Merrut': '#react-select-4-option-2'
        }

        selector = city_map.get(city, '#react-select-4-option-0')
        browser.element(selector).click()
        return self

    def click_submit(self):
        self.submit_button.click()
        return self