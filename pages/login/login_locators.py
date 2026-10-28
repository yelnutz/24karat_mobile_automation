"""Replace these example accessibility IDs using Appium Inspector."""

from appium.webdriver.common.appiumby import AppiumBy


class LoginLocators:
    # Set to True only after replacing all example locators below.
    CONFIGURED = False

    USERNAME = (AppiumBy.ACCESSIBILITY_ID, "login_username")
    PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "login_password")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "login_button")
    ERROR_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "login_error")
    HOME_SCREEN = (AppiumBy.ACCESSIBILITY_ID, "home_screen")
