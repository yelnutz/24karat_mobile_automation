"""Shared actions using explicit waits."""

from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver, timeout: float = 15):
        self.driver = driver
        self.timeout = timeout

    def wait_for_visible(self, locator: Locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def tap(self, locator: Locator) -> None:
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator: Locator, text: str) -> None:
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Locator) -> str:
        return self.wait_for_visible(locator).text

    def is_present(self, locator: Locator) -> bool:
        """Check for an element without an explicit wait or action if absent.

        Presence does not require the element to be visible or clickable.
        """
        return bool(self.driver.find_elements(*locator))

    def is_visible(self, locator: Locator) -> bool:
        try:
            self.wait_for_visible(locator)
            return True
        except TimeoutException:
            return False
