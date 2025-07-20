from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set capabilities for goRentals app
options = UiAutomator2Options()
options.platform_name = "android"
options.platform_version = "14"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"
options.app = "/Users/mohanprasad/Documents/goRentals.apk"
options.auto_grant_permissions = True
options.app_activity = "com.gorentals.goappprev.MainActivity"
options.app_package = "com.gorentals.goappprev"

# Additional useful options
options.new_command_timeout = 300  # 5 minutes timeout
options.no_reset = False  # Install app fresh each time

# Initialize the driver
driver = webdriver.Remote("http://localhost:4723", options=options)

try:
    print("Successfully connected to goRentals app!")
    
    # Wait for app to load
    wait = WebDriverWait(driver, 30)
    
    # Print current activity to understand app state
    print(f"Current Activity: {driver.current_activity}")
    print(f"Current Package: {driver.current_package}")
    
    # Take initial screenshot
    driver.save_screenshot("test_outputs/gorentals_launch.png")
    print("Initial screenshot saved as test_outputs/gorentals_launch.png")
    
    # Wait a bit for the app to fully load
    time.sleep(5)
    
    # Example: Try to find elements by different strategies
    # You'll need to inspect the app to find actual element IDs/text
    
    print("\nLooking for UI elements...")
    
    # Try to find elements by text (common in rental apps)
    try:
        # Look for common rental app elements
        search_texts = ["Search", "Login", "Sign In", "Get Started", "Skip", "Allow", "Next"]
        
        for text in search_texts:
            try:
                element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                    f'new UiSelector().textContains("{text}")')
                print(f"Found element with text: {text}")
                # Take screenshot when element is found
                driver.save_screenshot(f"test_outputs/gorentals_found_{text.lower().replace(' ', '_')}.png")
            except:
                pass
    except Exception as e:
        print(f"Error finding elements by text: {e}")
    
    # Try to find clickable elements
    try:
        clickable_elements = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 
            'new UiSelector().clickable(true)')
        print(f"\nFound {len(clickable_elements)} clickable elements")
    except:
        print("Could not find clickable elements")
    
    # Get page source for debugging
    page_source = driver.page_source
    
    # Save page source to file for analysis
    with open("test_outputs/gorentals_page_source.xml", "w", encoding="utf-8") as f:
        f.write(page_source)
    print("\nPage source saved to test_outputs/gorentals_page_source.xml")
    
    # Example automation flow (you'll need to customize based on your app)
    print("\n--- Sample Automation Flow ---")
    
    # 1. Handle any initial popups/permissions
    # Example: Skip intro or allow permissions
    try:
        skip_button = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Skip")')))
        skip_button.click()
        print("Clicked Skip button")
    except:
        print("No Skip button found")
    
    # 2. Navigate to main features
    # This is where you'd add your specific test scenarios
    
    # Take final screenshot
    time.sleep(2)
    driver.save_screenshot("test_outputs/gorentals_final_state.png")
    print("\nFinal screenshot saved")
    
    print("\n=== Test completed successfully! ===")
    print("\nNext steps:")
    print("1. Check test_outputs/gorentals_page_source.xml to see all available elements")
    print("2. Look at the screenshots in test_outputs/ to understand the UI")
    print("3. Update this script with specific element locators and test scenarios")
    
except Exception as e:
    print(f"\nError occurred: {e}")
    driver.save_screenshot("test_outputs/gorentals_error.png")
    print("Error screenshot saved")
    
finally:
    print("\nClosing driver...")
    driver.quit() 