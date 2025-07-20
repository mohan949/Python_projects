from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Set capabilities
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"
options.no_reset = True
# Don't specify app_package/app_activity to start with current screen

# Initialize the Appium driver
driver = webdriver.Remote("http://localhost:4723", options=options)

try:
    print("Connected to device successfully!")
    
    # Get device info
    print(f"\nDevice Info:")
    print(f"Platform: {driver.capabilities['platformName']}")
    print(f"Platform Version: {driver.capabilities['platformVersion']}")
    print(f"Device Name: {driver.capabilities['deviceName']}")
    print(f"Automation: {driver.capabilities['automationName']}")
    
    # Get current activity
    current_activity = driver.current_activity
    current_package = driver.current_package
    print(f"\nCurrent App: {current_package}")
    print(f"Current Activity: {current_activity}")
    
    # Get screen size
    screen_size = driver.get_window_size()
    print(f"\nScreen Size: {screen_size['width']}x{screen_size['height']}")
    
    # Perform some basic gestures
    print("\nPerforming basic gestures...")
    
    # Swipe down (pull notification shade)
    start_x = screen_size['width'] // 2
    start_y = 10
    end_y = screen_size['height'] // 2
    
    driver.swipe(start_x, start_y, start_x, end_y, 500)
    print("Swiped down to show notifications")
    time.sleep(2)
    
    # Press back button to dismiss notifications
    driver.press_keycode(4)  # 4 is the keycode for BACK button
    print("Pressed back button")
    time.sleep(1)
    
    # Open quick settings
    driver.open_notifications()
    print("Opened notifications panel")
    time.sleep(2)
    
    # Press home button
    driver.press_keycode(3)  # 3 is the keycode for HOME button
    print("Pressed home button")
    time.sleep(1)
    
    # Take a screenshot
    driver.save_screenshot("test_outputs/basic_test_screenshot.png")
    print("\nScreenshot saved as test_outputs/basic_test_screenshot.png")
    
    print("\nBasic Appium test completed successfully!")
    
except Exception as e:
    print(f"Error occurred: {e}")
    
finally:
    driver.quit()
    print("Driver closed.") 