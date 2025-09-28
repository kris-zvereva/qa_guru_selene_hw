import os
from selene import browser, have, command

def test_submit_practice_form(set_browser):
    browser.open('/automation-practice-form')

    # Personal information
    browser.element('#firstName').type('First Name')
    browser.element('#lastName').type('Last Name')
    browser.element('#userEmail').type('email@test.qa')
    browser.element('label[for="gender-radio-2"]').perform(command.js.scroll_into_view).click()
    browser.element('#userNumber').type('1234567890')

    # Date of birth
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="8"]').click()
    browser.element('.react-datepicker__year-select option[value="1999"]').click()
    browser.element('[aria-label="Choose Wednesday, September 1st, 1999"]').click()

    # Subjects and hobbies
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('label[for="hobbies-checkbox-2"]').click()

    # Image upload
    file_path = os.path.abspath('test_image.png')
    browser.element('#uploadPicture').send_keys(file_path)

    # Address
    browser.element('#currentAddress').type('test address')
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Karnal').press_enter()

    browser.element('#submit').click()

    # Verification
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tr').should(have.texts(
        'Label Values',
        'Student Name First Name Last Name',
        'Student Email email@test.qa',
        'Gender Female',
        'Mobile 1234567890',
        'Date of Birth 01 September,1999',
        'Subjects Maths',
        'Hobbies Reading',
        'Picture test_image.png',
        'Address test address',
        'State and City Haryana Karnal'
    ))