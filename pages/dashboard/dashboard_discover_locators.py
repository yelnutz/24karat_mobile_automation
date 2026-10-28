"""Replace these example accessibility IDs using Appium Inspector."""

from appium.webdriver.common.appiumby import AppiumBy


class loginPageLocators:
    # Set to True only after replacing all example locators below.
    CONFIGURED = False

    TUTORIAL_SHOWME_BTN = (AppiumBy.ACCESSIBILITY_ID, "Show me around")
    
    TUTORIAL_SKIP_BTN = (AppiumBy.ACCESSIBILITY_ID, "Skip for now")
    
    TUTORIAL_NEXT_BTN = (AppiumBy.ACCESSIBILITY_ID, "Next")
    
    TUTORIAL_BACK_BTN = (AppiumBy.ACCESSIBILITY_ID, "Back")
    
    TUTORIAL_SKIP_BTN = (AppiumBy.ACCESSIBILITY_ID, "Skip")
    
    TUTORIAL_STEP1_TEXT = (AppiumBy.ACCESSIBILITY_ID, "Join the fun")
    
    TUTORIAL_STEP2_TEXT = (AppiumBy.ACCESSIBILITY_ID, "Two kinds of points")
    
    TUTORIAL_STEP3_TEXT = (AppiumBy.ACCESSIBILITY_ID, "24k Points")
    
    TUTORIAL_STEP4_TEXT = (AppiumBy.ACCESSIBILITY_ID, "Unlock exclusive rewards")
    
    TUTORIAL_LASTWINDOW_TEXT1 = (AppiumBy.ACCESSIBILITY_ID, "Pick your favorite brands")
    
    TUTORIAL_LASTWINDOW_TEXT2 = (AppiumBy.ACCESSIBILITY_ID, "Complete community missions")
    
    TUTORIAL_LASTWINDOW_TEXT3 = (AppiumBy.ACCESSIBILITY_ID, "Collect points and Fan Items")
    
    TUTORIAL_LASTWINDOW_PICKBRANDS_BTN = (AppiumBy.ACCESSIBILITY_ID, "Pick my brands")
    
    NOTIFICATION_YES_BTN = (AppiumBy.ACCESSIBILITY_ID, "Turn on")
    
    NOTIFICATION_NO_BTN = (AppiumBy.ACCESSIBILITY_ID, "No, Thanks")
    
    ALLOW_NOTIFICATIONS = (
        AppiumBy.ID,
        "com.android.permissioncontroller:id/permission_allow_button"
    )

    DENY_NOTIFICATIONS = (
        AppiumBy.ID,
        "com.android.permissioncontroller:id/permission_deny_button"
    )

    """
    MAIN_RESEND_OTPBTN = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Resend")')
    
    MAIN_OTPTEXTFIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Enter the code").className("android.widget.EditText")')
    """
    
    