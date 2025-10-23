from high_level_step_objects.data import users
from high_level_step_objects.model.pages.registration_page import RegistrationPage


def test_submit_practice_form(set_browser):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(users.student)
    registration_page.submit()

    registration_page.should_have_modal_text('Thanks for submitting the form')
    registration_page.should_have_registered(users.student)