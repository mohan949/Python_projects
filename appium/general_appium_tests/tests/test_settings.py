from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Set capabilities using AppiumOptions
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"  # Use your device name from `adb devices`
options.app_package = "com.android.settings"  # Settings app package
options.app_activity = ".Settings"  # Main Settings activity
options.automation_name = "UiAutomator2"
options.no_reset = True

# Initialize the Appium driver
driver = webdriver.Remote("http://localhost:4723", options=options)

try:
    # Give the app some time to load
    time.sleep(2)
    
    print("Successfully launched Settings app!")
    
    # Find and click on "About phone" or similar option
    # The exact text might vary by Android version
    try:
        # Try to find "About phone" (common in many Android versions)
        about_element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                          'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(text("About phone"))')
        about_element.click()
        print("Clicked on 'About phone'")
    except:
        try:
            # Alternative: Try "About emulated device" for emulators
            about_element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                              'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(text("About emulated device"))')
            about_element.click()
            print("Clicked on 'About emulated device'")
        except:
            print("Could not find About section, but Settings app is working!")
    
    # Wait a bit to see the result
    time.sleep(3)
    
    # Take a screenshot for verification
    driver.save_screenshot("test_outputs/settings_screenshot.png")
    print("Screenshot saved as test_outputs/settings_screenshot.png")
    
finally:
    # Always quit the driver
    driver.quit()
    print("Test completed!") 