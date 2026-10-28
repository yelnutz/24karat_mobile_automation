"""Starter scenarios: replace locators and configure the target app first."""

import os

import pytest

from pages.login.login_actions import LoginActions
from pages.login.login_locators import LoginLocators

pytestmark = [
    pytest.mark.android,
    pytest.mark.login,
    pytest.mark.skipif(
        not LoginLocators.CONFIGURED,
        reason="Replace example login locators and set CONFIGURED = True first.",
    ),
]


def test_login_screen_is_displayed(driver):
    assert LoginActions(driver).is_login_displayed()


def test_login_with_valid_credentials(driver):
    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")
    if not username or not password:
        pytest.skip("Set TEST_USERNAME and TEST_PASSWORD for a valid test account.")
    login = LoginActions(driver)
    login.login(username, password)
    assert login.is_home_displayed()


def test_login_with_invalid_credentials(driver):
    expected_error = os.getenv("LOGIN_EXPECTED_ERROR")
    if not expected_error:
        pytest.skip("Set LOGIN_EXPECTED_ERROR to the app's expected error message.")
    login = LoginActions(driver)
    login.login("invalid-user@example.invalid", "invalid-password")
    assert login.get_error_message() == expected_error
