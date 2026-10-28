# Mobile automation

Python + pytest + Appium, with screen locators and interactions separated from tests.

## Setup (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
npm install
npm run driver:install
npm run driver:doctor
```

On this machine the default `npm` shim points to a missing installation. Until
that PATH entry is repaired, replace `npm` in these commands with
`& 'D:\Apps\Nodejs\npm.cmd'` in PowerShell.

Install an Android SDK and Java supported by the UiAutomator2 driver. Configure
ANDROID_HOME and JAVA_HOME, and start an emulator or connect a device with USB
debugging enabled. Use `adb devices` to find its UDID. Appium's npm installer
checks the supported Node.js version.

## Configure your app

```powershell
$env:ANDROID_UDID = 'emulator-5554'
$env:ANDROID_APP = 'C:\path\to\your-app.apk'
# For an installed app, omit ANDROID_APP and set both instead:
# $env:ANDROID_APP_PACKAGE = 'your.app.package'
# $env:ANDROID_APP_ACTIVITY = 'your.app.MainActivity'
$env:TEST_USERNAME = 'your-test-account'
$env:TEST_PASSWORD = 'your-test-password'
# Optional: required for the invalid-login scenario
$env:LOGIN_EXPECTED_ERROR = 'Your exact login error message'
```

Replace the accessibility IDs in `pages/login/login_locators.py` with real app
locators from Appium Inspector, then set `LoginLocators.CONFIGURED = True`.
The example assumes a fresh session opens the login screen; adapt app setup if
your app restores a signed-in account or displays onboarding first.
Environment variables are read directly; `.env` files are not automatically loaded.

Start the server in one terminal:

```powershell
npm run appium
```

Run tests in another terminal with the app environment variables configured:

```powershell
.\venv\Scripts\python.exe -m pytest
.\venv\Scripts\python.exe -m pytest -m login
```

Tests skip until the locators and app configuration are supplied. A successful
local scaffold check does not verify device interaction. Each test receives a
new session, and the fixture closes it even if the test fails.

Optional settings: ANDROID_DEVICE_NAME, ANDROID_PLATFORM_VERSION, APPIUM_SERVER_URL
(default `http://127.0.0.1:4723`). Generated environments, Node dependencies,
app binaries, and credentials are excluded from Git.
