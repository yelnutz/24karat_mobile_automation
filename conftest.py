"""A fresh Appium session for each test, always closed after use."""

import os

import pytest

from utils.driver_factory import create_driver


@pytest.fixture
def driver():
    if not os.getenv("ANDROID_APP") and not (
        os.getenv("ANDROID_APP_PACKAGE") and os.getenv("ANDROID_APP_ACTIVITY")
    ):
        pytest.skip("Configure ANDROID_APP or ANDROID_APP_PACKAGE/ANDROID_APP_ACTIVITY.")
    session = create_driver()
    try:
        yield session
    finally:
        session.quit()
