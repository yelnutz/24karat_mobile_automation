"""Replace these example accessibility IDs using Appium Inspector."""

from appium.webdriver.common.appiumby import AppiumBy


class loginPageLocators:
    # Set to True only after replacing all example locators below.
    CONFIGURED = False

    MAIN_NEXTBTN = (AppiumBy.ACCESSIBILITY_ID, "Next")
    
    MAIN_SKIPBTN = (AppiumBy.ACCESSIBILITY_ID, "Skip")
    
    MAIN_EMAIL_TEXTFIELD = (AppiumBy.ACCESSIBILITY_ID, "Email")
    
    MAIN_LOGIN_PHONE = (AppiumBy.ACCESSIBILITY_ID, "Using phone number")
    
    MAIN_LOGIN_PASSPHRASE = (AppiumBy.ACCESSIBILITY_ID, "Using pass phrase")
    
    MAIN_LOGINBTN = (AppiumBy.ACCESSIBILITY_ID, "Log in")
    
    MAIN_RESEND_OTPBTN = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Resend")')
    
    MAIN_OTPTEXTFIELD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Enter the code").className("android.widget.EditText")')
    
    MAIN_LOGIN_CONTINUEBTN = (AppiumBy.ACCESSIBILITY_ID, "Continue")
    
    