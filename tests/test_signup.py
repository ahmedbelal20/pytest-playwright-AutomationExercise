from playwright.sync_api import expect, Page
from logging import Logger, getLogger

logger: Logger = getLogger(__name__)

from pages.signup_page import LoginPage
from enums.constants import Url, Text, Title

def test_signup_correct(page: Page):
    # Launch browser, go to base URL, and verify correct navigation
    page.goto(Url.BASE.value)
    expect(page).to_have_url(Url.BASE.value)
    expect(page).to_have_title(Title.HOME.value)
    # Click on the Signup / Login button and verify correct navigation to /login page
    page.get_by_text(Text.BUTTON_SIGNUP.value, exact=True).click()
    expect(page).to_have_url(Url.SIGNUP.value)
    expect(page).to_have_title(Title.SIGNUP.value)
    # Fill the sign up form
    login_page = LoginPage(page)
    login_page.enter_signup_name("Belal")
    login_page.enter_signup_email("belal@domain.com")
    # Click sign up
    login_page.click_signup()