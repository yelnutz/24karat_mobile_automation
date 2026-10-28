
"""Android configuration for Appium automation."""

import os

from appium.options.android import UiAutomator2Options


APP_PACKAGE = "io.zap_24k.dev"


def get_android_options() -> UiAutomator2Options:
    """Configure Appium for an already installed Android app."""

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"

    # Android emulator configuration
    options.device_name = os.getenv(
        "ANDROID_DEVICE_NAME", "emulator-5554"
    )
    options.udid = os.getenv(
        "ANDROID_UDID", "emulator-5554"
    )

    # Preserve installed app and existing user data
    options.no_reset = True

    # Appium session timeout
    options.new_command_timeout = 120

    return options
