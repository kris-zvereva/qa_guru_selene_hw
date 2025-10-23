import os

from selene import browser, have, command

from high_level_step_objects.data.user import User, Gender, Hobby


REGISTRATION_PAGE_URL = 'https://demoqa.com/automation-practice-form'
IMAGE_PATH = 'resources/test_image.png'

class RegistrationPage:
    def __init__(self):
        self.url = REGISTRATION_PAGE_URL
        self.file_path = os.path.abspath(IMAGE_PATH)
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.phone_input = browser.element('#userNumber')
        self.state = browser.element('#state')


    def open(self):
        browser.open(self.url)
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def _fill_first_name(self, first_name):
        self.first_name.type(first_name)

    def _fill_last_name(self, last_name):
        self.last_name.type(last_name)

    def _fill_email(self, email):
        self.email.type(email)

    def _select_gender(self, gender: Gender):
        gender_map = {
            Gender.MALE: '1',
            Gender.FEMALE: '2',
            Gender.OTHER: '3'
        }
        browser.element(f'label[for="gender-radio-{gender_map[gender]}"]').click()

    def _fill_phone(self, phone):
        self.phone_input.type(phone)

    def _fill_date_of_birth(self, day, month, year):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('[class="react-datepicker__month-select"]').click()
        browser.element(f'.//option[@value={month}]').click()
        browser.element('[class="react-datepicker__year-select"]').click()
        browser.element(f'[value="{year}"]').click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--00{day}"]').click()

    def _select_hobbies(self, *hobbies: Hobby):
        hobby_map = {
            Hobby.SPORTS: '1',
            Hobby.READING: '2',
            Hobby.MUSIC: '3'
        }
        for hobby in hobbies:
            browser.element(f'label[for="hobbies-checkbox-{hobby_map[hobby]}"]').click()

    def _fill_subjects(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def _upload_image(self):
        browser.element('#uploadPicture').send_keys(self.file_path)

    def _fill_address(self, text_address):
        browser.element('#currentAddress').type(text_address)

    def _fill_state_and_city(self, state, city):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()
        browser.element('#city').click()
        browser.element('#react-select-4-input').type(city).press_enter()

    def should_have_modal_text(self, text):
        browser.element('#example-modal-sizes-title-lg').should(have.text(text))

    def should_have_registered(self, user: User):
        hobbies_str = ', '.join(h.value for h in user.hobbies)

        browser.all('tr').should(have.texts(
            'Label Values',
            f'Student Name {user.full_name}',
            f'Student Email {user.email}',
            f'Gender {user.gender.value}',
            f'Mobile {user.phone}',
            f'Date of Birth {user.formatted_date_of_birth}',
            f'Subjects {user.subjects}',
            f'Hobbies {hobbies_str}',
            f'Picture {user.picture}',
            f'Address {user.address}',
            f'State and City {user.state} {user.city}'
        ))

    def register(self, user: User):
        self._fill_first_name(user.first_name)
        self._fill_last_name(user.last_name)
        self._fill_email(user.email)
        self._select_gender(user.gender)
        self._fill_phone(user.phone)
        self._fill_date_of_birth(
            day=user.date_of_birth.day,
            month=user.date_of_birth.month - 1,
            year=user.date_of_birth.year
        )
        self._select_hobbies(*user.hobbies)
        self._fill_subjects(user.subjects)
        self._upload_image()
        self._fill_address(user.address)
        self._fill_state_and_city(user.state, user.city)

    def submit(self):
        browser.element('#submit').click()
