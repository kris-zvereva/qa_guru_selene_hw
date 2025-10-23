from mid_level_step_objects_done.model.pages.registration_page import RegistrationPage


def test_submit_practice_form(set_browser):
    registration_page = RegistrationPage()
    registration_page.open()
    # Personal information
    registration_page.fill_first_name('First Name')
    registration_page.fill_last_name('Last Name')
    registration_page.fill_email('email@test.qa')
    registration_page.select_gender('Female')
    registration_page.fill_phone('1234567890')
    # Date of birth
    registration_page.fill_dob(1, 8, 1999)
    # Subjects and hobbies
    registration_page.select_hobbies('Reading')
    registration_page.fill_subjects('Maths')
    # Image upload
    registration_page.upload_image()
    # Address
    registration_page.fill_address('test address')
    registration_page.fill_state_and_city('Haryana', 'Karnal')
    registration_page.submit()
    # Verification
    registration_page.should_have_modal_text('Thanks for submitting the form')
    registration_page.should_have_registered(
        ('Student Name', 'First Name Last Name'),
        ('Student Email', 'email@test.qa'),
        ('Gender', 'Female'),
        ('Mobile', '1234567890'),
        ('Date of Birth', '01 September,1999'),
        ('Subjects', 'Maths'),
        ('Hobbies', 'Reading'),
        ('Picture', 'test_image.png'),
        ('Address', 'test address'),
        ('State and City', 'Haryana Karnal')
    )