import os
from selene.core import command
from selene.support.shared import browser
from selene import be, have, command
import pytest

#@pytest.fixture(scope="function", autouse=True)
@pytest.fixture(autouse=True)
def browser_management():
    browser.config.timeout = 3
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1024
    browser.config.window_height = 2000
    yield


def test_registration_form(browser_management):
    browser.open('/automation-practice-form')
    browser.should(have.title('ToolsQA'))

    # Name
    browser.element('#firstName').should(be.blank).type('Olga').press_enter()
    browser.element('#lastName').should(be.blank).type('Kos').press_enter()
    browser.element('#userEmail').should(be.blank).type('test@test.uk').press_enter()

    # Phone number
    browser.element('#userNumber').should(be.blank).type('1112233445').press_enter()

    # Gender
    #browser.element('#gender-radio-2').press_enter()
    browser.element("[for='gender-radio-2']").click()

    # Subjects
    #browser.element('.subjects-auto-complete__placeholder').set_value("Arts").press_enter()
    # browser.element('.subjects-auto-complete__placeholder').set_value("English").press_enter()
    browser.element('#subjectsInput').type('Arts').press_enter().type('English').press_enter()

    # Form with date
    #browser.element('#dateOfBirthInput').should(be.blank).set_value("23 Apr 1995").press_enter()

    browser.element('#dateOfBirth-wrapper').click()
    browser.element('.react-datepicker__month-select').type("April")
    browser.element('.react-datepicker__year-select').type("1995")
    browser.element('[aria-label= "Choose Sunday, April 23rd, 1995"]').click()

    # Hobbies
    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element("[for='hobbies-checkbox-3']").click()

    # Loading a picture
    browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/siegfriedsassoon.jpg'))

    # Address
    browser.element('#currentAddress').type('Peterburg, Moskowsky 16')

    # Dropdowns
    browser.element('#state').perform(command.js.scroll_into_view).click()

    # State selection
    browser.element('#state').click()
    browser.element('#state input').type('Rajasthan').press_enter()

    # City selection
    browser.element('#city').click()
    browser.element('#city input').type('Jaipur').press_enter()

    # Submit form button
    browser.element('#submit').press_enter()

    #browser.wait_until(10000)

    #Check

    #<div class="modal-title h4" id="example-modal-sizes-title-lg">Thanks for submitting the form</div>
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element("//td[text()='Student Name']").element("..").should(have.text('Olga Kos'))
    browser.element("//td[text()='Student Email']").element("..").should(have.text('test@test.uk'))

    browser.element("//td[text()='Gender']").element("..").should(have.text('Female'))
    browser.element("//td[text()='Mobile']").element("..").should(have.text('1112233445'))

    browser.element("//td[text()='Date of Birth']").element("..").should(have.text('23 April,1995'))
    browser.element("//td[text()='Subjects']").element("..").should(have.text('Arts, English'))

    browser.element("//td[text()='Hobbies']").element("..").should(have.text('Reading, Music'))
    browser.element("//td[text()='Picture']").element("..").should(have.text('siegfriedsassoon.jpg'))

    browser.element("//td[text()='Address']").element("..").should(have.text('Peterburg, Moskowsky 16'))
    browser.element("//td[text()='State and City']").element("..").should(have.text('Rajasthan Jaipur'))

def test2():
    pass