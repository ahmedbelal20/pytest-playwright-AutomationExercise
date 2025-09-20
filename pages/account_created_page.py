from playwright.sync_api import Page, Locator


class AccountCreatedPage():

    def __init__(self, page: Page) -> None:
        self.page = page
        self.continue_button: Locator = page.locator("a[data-qa='continue-button']")

    def click_continue(self) -> None:
        self.continue_button.click()