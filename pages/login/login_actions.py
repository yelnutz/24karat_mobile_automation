"""Reusable login interactions; assertions belong in tests."""
import allure
from pages.base_page import BasePage
from pages.login.login_locators import LoginLocators
from pages.login.login_locators import dashboardLocators


class LoginActions(BasePage):
    def is_login_displayed(self) -> bool:
        return self.is_visible(LoginLocators.LOGIN_BUTTON)

    def is_home_displayed(self) -> bool:
        return self.is_visible(LoginLocators.HOME_SCREEN)

    def get_error_message(self) -> str:
        return self.get_text(LoginLocators.ERROR_MESSAGE)

    @allure.step("Check if first time login")
    def is_first_time_login(self) -> bool:
        if self.is_present(dashboardLocators.SKIPBTN):
            self.tap(dashboardLocators.SKIPBTN)
            return True
        return False
    
    @allure.step("Log in on the app with email")
    def login_input_email(self, username: str) -> None:
            self.enter_text(LoginLocators.USERNAME, username)
            self.tap(LoginLocators.LOGIN_BUTTON)
            
    @allure.step("Input OTP code")
    def login_input_otp(self, otp_code: str) -> None:
            self.enter_text(LoginLocators.OTP_TEXTFIELD, otp_code)