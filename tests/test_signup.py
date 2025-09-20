from playwright.sync_api import expect, Page
from logging import Logger, getLogger

logger: Logger = getLogger(__name__)

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_created_page import AccountCreatedPage
from pages.account_deleted_page import AccountDeletedPage
from enums.constants import Url, Text, Title

def test_signup_correct(page: Page):
    # Launch browser, go to base URL, and verify correct navigation
    page.goto(Url.HOME.value)
    expect(page).to_have_url(Url.HOME.value)
    expect(page).to_have_title(Title.HOME.value)
    # Click on the Signup / Login button
    home_page = HomePage(page)
    home_page.click_login_signup()
    # Verify correct navigation
    expect(page).to_have_url(Url.LOGIN.value)
    expect(page).to_have_title(Title.LOGIN.value)
    # Fill the sign up form
    login_page = LoginPage(page)
    login_page.enter_signup_name("John Doe")
    login_page.enter_signup_email("JohnnyDoey@domain.com")
    # Click sign up and verify correct navigation
    login_page.click_signup()
    expect(page).to_have_url(Url.SIGNUP.value)
    expect(page).to_have_title(Title.SIGNUP.value)
    # Fill sign up details
    signup_page = SignupPage(page)
    signup_page.select_gender_male()
    signup_page.enter_password("JD12345")
    signup_page.select_birth_day("1")
    signup_page.select_birth_month("January")
    signup_page.select_birth_year("2000")
    signup_page.select_newsletter_signup()
    signup_page.select_offers_signup()
    signup_page.enter_first_name("John")
    signup_page.enter_last_name("Doe")
    signup_page.enter_company("The Johnnys")
    signup_page.enter_address("Johny Home")
    signup_page.enter_address2("Doey Home")
    signup_page.select_country("United States")
    signup_page.enter_state("The Staties")
    signup_page.enter_city("The Cities")
    signup_page.enter_zipcode("The Zippies")
    signup_page.enter_mobile_number("011111111")
    signup_page.click_create_account()
    # Account creation complete
    expect(page).to_have_url(Url.ACCOUNT_CREATED.value)
    expect(page).to_have_title(Title.ACCOUNT_CREATED.value)
    account_created_page = AccountCreatedPage(page)
    account_created_page.click_continue()
    # Home page - logged in
    expect(page).to_have_url(Url.HOME.value)
    expect(page).to_have_title(Title.HOME.value)
    home_page = HomePage(page)
    home_page.verify_logged_in_status("John Doe")
    home_page.click_delete_account()
    # Verify correct navigation
    expect(page).to_have_url(Url.DELETE_ACCOUNT.value)
    expect(page).to_have_title(Title.DELETE_ACCOUNT.value)
    account_deleted_page = AccountDeletedPage(page)
    account_deleted_page.click_continue()
    # Verify correct navigation
    expect(page).to_have_url(Url.HOME.value)
    expect(page).to_have_title(Title.HOME.value)
    home_page = HomePage(page)
    home_page.verify_logged_out_status()
