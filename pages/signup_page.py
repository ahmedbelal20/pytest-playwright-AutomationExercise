from playwright.sync_api import Page, Locator


class SignupPage():

    def __init__(self, page: Page) -> None:
        self.page = page
        self.signup_form: Locator = page.locator("form[action='/signup']")
        # Account information locators
        self.gender_male_button: Locator = self.signup_form.locator("input[type='radio'][name='title'][id='id_gender1'][value='Mr']")
        self.gender_female_button: Locator = self.signup_form.locator("input[type='radio'][name='title'][id='id_gender2'][value='Mrs']")
        self.password: Locator = self.signup_form.locator("input[data-qa='password']")
        self.birth_day: Locator = self.signup_form.locator("select[data-qa='days']")
        self.birth_month: Locator = self.signup_form.locator("select[data-qa='months']")
        self.birth_year: Locator = self.signup_form.locator("select[data-qa='years']")
        self.newsletter_signup: Locator = self.signup_form.locator("input[type='checkbox'][name='newsletter']")
        self.offers_signup: Locator = self.signup_form.locator("input[type='checkbox'][name='optin']")
        # Address information locators
        self.first_name: Locator = self.signup_form.locator("input[data-qa='first_name']")
        self.last_name: Locator = self.signup_form.locator("input[data-qa='last_name']")
        self.company: Locator = self.signup_form.locator("input[data-qa='company']")
        self.address: Locator = self.signup_form.locator("input[data-qa='address']")
        self.address2: Locator = self.signup_form.locator("input[data-qa='address2']")
        self.country: Locator = self.signup_form.locator("select[data-qa='country']")
        self.state: Locator = self.signup_form.locator("input[data-qa='state']")
        self.city: Locator = self.signup_form.locator("input[data-qa='city']")
        self.zipcode: Locator = self.signup_form.locator("input[data-qa='zipcode']")
        self.mobile_number: Locator = self.signup_form.locator("input[data-qa='mobile_number']")
        # Button
        self.create_account_button: Locator = self.signup_form.locator("button[data-qa='create-account']")

    def select_gender_male(self) -> None:
        self.gender_male_button.click()

    def select_gender_female(self) -> None:
        self.gender_female_button.click()

    def enter_password(self, password: str) -> None:
        self.password.fill(password)

    def select_birth_day(self, day: str) -> None:
        self.birth_day.select_option(day)

    def select_birth_month(self, month: str) -> None:
        self.birth_month.select_option(month)

    def select_birth_year(self, year: str) -> None:
        self.birth_year.select_option(year)

    def select_newsletter_signup(self) -> None:
        self.newsletter_signup.click()

    def select_offers_signup(self) -> None:
        self.offers_signup.click()

    def enter_first_name(self, name: str) -> None:
        self.first_name.fill(name)

    def enter_last_name(self, name: str) -> None:
        self.last_name.fill(name)

    def enter_company(self, company: str) -> None:
        self.company.fill(company)

    def enter_address(self, address: str) -> None:
        self.address.fill(address)

    def enter_address2(self, address: str) -> None:
        self.address2.fill(address)

    def select_country(self, country: str) -> None:
        self.country.select_option(country)

    def enter_state(self, state: str) -> None:
        self.state.fill(state)

    def enter_city(self, city: str) -> None:
        self.city.fill(city)

    def enter_zipcode(self, zipcode: str) -> None:
        self.zipcode.fill(zipcode)

    def enter_mobile_number(self, mobile_number: str) -> None:
        self.mobile_number.fill(mobile_number)

    def click_create_account(self) -> None:
        self.create_account_button.click()