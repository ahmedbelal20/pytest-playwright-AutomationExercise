from playwright.sync_api import Page, Locator


class SignupPage():

    def __init__(self, page: Page) -> None:
        self.page = page
        self.signup_form: Locator = page.locator("form[action='/signup']")
        self.gender_male_button: Locator = self.signup_form.locator("input[type='radio'][name='title'][id='id_gender1'][value='Mr']")
        self.gender_female_button: Locator = self.signup_form.locator("input[type='radio'][name='title'][id='id_gender2'][value='Mrs']")
        self.signup_password: Locator = self.signup_form.locator("input[data-qa='password']")

    def select_gender_male(self) -> None:
        self.gender_male_button.click()

    def select_gender_female(self) -> None:
        self.gender_female_button.click()

    def enter_password(self, password: str) -> None:
        self.signup_password.fill(password)
