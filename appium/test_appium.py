from appium import webdriver
from appium.options.android import UiAutomator2Options  # Use UiAutomator2Options for Android apps
import time

# Set capabilities using AppiumOptions
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"  # Emulator ID from `adb devices` (or use your physical device name)
options.app_package = "com.android.calculator2"  # Android Calculator app package
options.app_activity = ".Calculator"  # Activity to launch the Calculator
options.automation_name = "UiAutomator2"  # Use UiAutomator2 automation framework

# Initialize the Appium driver with the desired capabilities
#driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
driver = webdriver.Remote("http://localhost:4723", options=options)


# Give the app some time to load
time.sleep(2)

# Perform a simple calculation: 2 + 3
driver.find_element("id", "com.android.calculator2:id/digit_2").click()  # Click 2
driver.find_element("accessibility id", "plus").click()  # Click +
driver.find_element("id", "com.android.calculator2:id/digit_3").click()  # Click 3
driver.find_element("accessibility id", "equals").click()  # Click =

# Get the result of the calculation
result = driver.find_element("id", "com.android.calculator2:id/result").text
print(f"Calculation result: {result}")  # Should print: 5

# Quit the driver after the test is done
driver.quit()
