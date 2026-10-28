import pytest

from config.capabilities import APP_PACKAGE
from utils.driver_factory import create_driver


@pytest.fixture(scope="session")
def driver():
    session = create_driver()

    try:
        # Launch the installed 24karat application
        session.activate_app(APP_PACKAGE)

        # Make driver available to all tests
        yield session

    finally:
        # Close Appium session after all tests finish
        session.quit()
