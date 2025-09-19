from playwright.sync_api import Page, Locator


class LoginPage():

    def __init__(self, page: Page) -> None:
        self.page = page
        self.signup_form: Locator = page.locator("form[action='/signup']")
        self.signup_name: Locator = self.signup_form.locator("input[data-qa='signup-name']")
        self.signup_email: Locator = self.signup_form.locator("input[data-qa='signup-email']")
        self.signup_button: Locator = self.signup_form.locator("button[data-qa='signup-button']")

    def enter_signup_name(self, name: str) -> None:
        self.signup_name.fill(name)

    def enter_signup_email(self, email: str) -> None:
        self.signup_email.fill(email)

    def click_signup(self) -> None:
        self.signup_button.click()