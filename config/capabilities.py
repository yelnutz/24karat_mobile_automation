"""Android settings supplied through environment variables."""

import os

from appium.options.android import UiAutomator2Options


def get_android_options() -> UiAutomator2Options:
    """Configure an APK or an already installed Android application."""
    app = os.getenv("ANDROID_APP")
    package = os.getenv("ANDROID_APP_PACKAGE")
    activity = os.getenv("ANDROID_APP_ACTIVITY")
    if not app and not (package and activity):
        raise ValueError(
            "Set ANDROID_APP to an APK path, or set both "
            "ANDROID_APP_PACKAGE and ANDROID_APP_ACTIVITY."
        )

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = os.getenv("ANDROID_DEVICE_NAME", "Android")
    options.no_reset = False
    options.new_command_timeout = 120
    if app:
        options.app = os.path.abspath(app)
    if package:
        options.app_package = package
    if activity:
        options.app_activity = activity
    if os.getenv("ANDROID_UDID"):
        options.udid = os.environ["ANDROID_UDID"]
    if os.getenv("ANDROID_PLATFORM_VERSION"):
        options.platform_version = os.environ["ANDROID_PLATFORM_VERSION"]
    return options
