from config.capabilities import APP_PACKAGE


def test_launch_app(driver):
    assert driver.current_package == APP_PACKAGE
    print("24karat app launched successfully!")
