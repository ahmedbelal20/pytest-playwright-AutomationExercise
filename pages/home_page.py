from playwright.sync_api import expect, Page, Locator


class HomePage():

    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_signup_button: Locator = page.locator("a[href='/login']")

    def click_login_signup(self) -> None:
        self.login_signup_button.click()

    def verify_logged_in_status(self, name: str) -> None:
        message: str = " Logged in as " + name + " "
        logged_in_message: Locator = self.page.get_by_text(message, exact=True)
        expect(logged_in_message).to_be_visible()

    def verify_logged_out_status(self) -> None:
        login_signup_button: Locator = self.page.locator("a[href='/login']")
        expect(login_signup_button).to_be_visible()

    def click_delete_account(self) -> None:
        self.page.locator("a[href='/delete_account']").click()