"""Create Appium sessions; the Appium server runs separately."""

import os

from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from config.capabilities import get_android_options


def create_driver() -> WebDriver:
    return webdriver.Remote(
        command_executor=os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723"),
        options=get_android_options(),
    )
