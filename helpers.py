import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoSuchElementException



def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def wait_for_element1(driver, locator, timeout=10):
    """Wait for the element to be visible"""
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def wait_and_type(driver, by_locator, text, timeout=10):
    """Wait for an element to be visible and type text into it."""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(by_locator)
        )
        element.send_keys(str(text))
    except TimeoutException:
        print(f"Timeout while waiting for {by_locator} to be visible.")
        raise


def wait_and_click(driver, by_locator, timeout=10):
    """Wait for an element to be clickable and then click on it."""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(by_locator)
        )
        element.click()
    except TimeoutException:
        print(f"Timeout while waiting for {by_locator} to be clickable.")
        raise


def wait_and_get_text(driver, locator, timeout=10):
    """Wait for the element to be visible and return its text."""
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
    return element.text


def assert_css_property(driver, selector, expected_properties):
    """General function to assert any CSS property."""
    try:
        element = driver.find_element(By.CSS_SELECTOR, selector)
        for prop, expected_value in expected_properties.items():
            actual_value = element.value_of_css_property(prop)
            # Ensure expected_value is string and avoid None issues
            expected_value = str(expected_value)
            assert expected_value in actual_value, f"Expected '{prop}' to contain '{expected_value}', but got '{actual_value}'"
        print("✅ All properties match expected values.")
    except AssertionError as e:
        print(f"❌ Assertion failed: {e}")
        raise
    except NoSuchElementException:
        print(f"❌ Element with selector '{selector}' not found.")
        raise
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        raise






