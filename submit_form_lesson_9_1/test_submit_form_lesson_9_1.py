import os
from selene import have
from registration_page import RegistrationPage


def test_student_registration_form(browser_management):
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.fill_first_name('Алексей')
    registration_page.fill_last_name('Антонов')
    registration_page.fill_email('antonov@example.com')
    registration_page.fill_gender()
    registration_page.fill_mobile_number('7951777777')
    registration_page.fill_date()
    registration_page.select_subjects('Maths')
    registration_page.select_hobbies()

    uploaded_filename = registration_page.load_picture()

    registration_page.fill_adress('Puskina, Kolotuskina, 123456789')
    registration_page.choice_state()
    registration_page.choice_city()
    registration_page.click_submit()

    registration_page.modal_window.should(have.text('Thanks for submitting the form'))

    registration_page.info_about_the_registered_user.should(have.exact_texts(
        'Алексей Антонов',
        'antonov@example.com',
        'Male',
        '7951777777',
        '27 July,1900',
        'Maths',
        'Music',
        uploaded_filename,
        'Puskina, Kolotuskina, 123456789',
        'NCR Delhi'
    ))

    # Очистка файла
    import tempfile
    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, uploaded_filename)
    if os.path.exists(temp_file_path):
        os.unlink(temp_file_path)