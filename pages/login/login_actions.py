"""Reusable login interactions; assertions belong in tests."""

from pages.base_page import BasePage
from pages.login.login_locators import LoginLocators


class LoginActions(BasePage):
    def login(self, username: str, password: str) -> None:
        self.enter_text(LoginLocators.USERNAME, username)
        self.enter_text(LoginLocators.PASSWORD, password)
        self.tap(LoginLocators.LOGIN_BUTTON)

    def is_login_displayed(self) -> bool:
        return self.is_visible(LoginLocators.LOGIN_BUTTON)

    def is_home_displayed(self) -> bool:
        return self.is_visible(LoginLocators.HOME_SCREEN)

    def get_error_message(self) -> str:
        return self.get_text(LoginLocators.ERROR_MESSAGE)
