from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_gorentals_registration():
    """Test the goRentals membership registration flow"""
    
    # Set capabilities
    options = UiAutomator2Options()
    options.platform_name = "android"
    options.platform_version = "14"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.app = "/Users/mohanprasad/Documents/goRentals.apk"
    options.auto_grant_permissions = True
    options.app_activity = "com.gorentals.goappprev.MainActivity"
    options.app_package = "com.gorentals.goappprev"
    options.no_reset = False  # Fresh install for testing
    
    driver = webdriver.Remote("http://localhost:4723", options=options)
    wait = WebDriverWait(driver, 20)
    
    try:
        logger.info("Successfully connected to goRentals app!")
        
        # Wait for app to load
        time.sleep(5)
        
        # Ensure test_outputs directory exists
        import os
        os.makedirs("test_outputs", exist_ok=True)
        
        # Take initial screenshot
        driver.save_screenshot("test_outputs/01_initial_screen.png")
        logger.info("Initial screenshot saved")
        
        # Check if we're on the registration screen
        try:
            # Find the "Congratulations!" text
            congrats_text = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR, 
                'new UiSelector().text("Congratulations!")'
            )
            logger.info("Found 'Congratulations!' text - We're on the registration screen")
        except:
            logger.warning("Not on expected registration screen")
        
        # Find and interact with the mobile number field
        try:
            # Find the EditText with hint "Mobile No."
            mobile_field = driver.find_element(
                AppiumBy.CLASS_NAME,
                "android.widget.EditText"
            )
            
            # Clear the default "+1" and enter a phone number
            mobile_field.clear()
            mobile_field.send_keys("+1234567890")
            logger.info("Entered mobile number: +1234567890")
            
            # Take screenshot after entering number
            driver.save_screenshot("test_outputs/02_mobile_entered.png")
            
        except Exception as e:
            logger.error(f"Could not find or interact with mobile field: {e}")
        
        # Find and click the terms and conditions checkbox
        try:
            # The checkbox is a ViewGroup that's clickable at bounds [70,2511][133,2574]
            # We'll try to find it by its clickable property and location
            checkbox = driver.find_element(
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@clickable="true" and @bounds="[70,2511][133,2574]"]'
            )
            checkbox.click()
            logger.info("Clicked terms and conditions checkbox")
            
            # Alternative method if xpath doesn't work
            # We can also try clicking by coordinates
            # driver.tap([(101, 2542)])  # Center of checkbox bounds
            
            time.sleep(1)
            driver.save_screenshot("test_outputs/03_checkbox_clicked.png")
            
        except Exception as e:
            logger.warning(f"Could not find checkbox by xpath, trying coordinates: {e}")
            try:
                # Click at the center of checkbox bounds
                driver.tap([(101, 2542)])
                logger.info("Clicked checkbox by coordinates")
                time.sleep(1)
                driver.save_screenshot("test_outputs/03_checkbox_clicked.png")
            except:
                logger.error("Could not click checkbox")
        
        # Check if the submit button is now enabled
        try:
            # The submit button is at bounds [72,2746][1368,2921] and was disabled
            submit_button = driver.find_element(
                AppiumBy.XPATH,
                '//android.view.ViewGroup[@clickable="true" and @bounds="[72,2746][1368,2921]"]'
            )
            
            # Check if it's enabled now
            if submit_button.is_enabled():
                logger.info("Submit button is now enabled")
                submit_button.click()
                logger.info("Clicked submit button")
                
                time.sleep(3)
                driver.save_screenshot("test_outputs/04_after_submit.png")
                
                # Check what happens after submission
                current_activity = driver.current_activity
                logger.info(f"Current activity after submit: {current_activity}")
                
            else:
                logger.info("Submit button is still disabled")
                # Try to find what else might be required
                driver.save_screenshot("test_outputs/04_button_still_disabled.png")
                
        except Exception as e:
            logger.error(f"Could not find or click submit button: {e}")
        
        # Additional exploration
        logger.info("\n=== Additional Information ===")
        
        # Get all text on screen
        text_elements = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        logger.info(f"Found {len(text_elements)} text elements:")
        for elem in text_elements:
            text = elem.text
            if text:
                logger.info(f"  - {text}")
        
        # Save final page source for debugging
        with open("test_outputs/gorentals_registration_page_source.xml", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        logger.info("\nPage source saved to test_outputs/gorentals_registration_page_source.xml")
        
        # Take final screenshot
        driver.save_screenshot("test_outputs/05_final_state.png")
        
        logger.info("\n=== Test completed! ===")
        
    except Exception as e:
        logger.error(f"Test failed with error: {e}")
        driver.save_screenshot("test_outputs/error_screenshot.png")
        
    finally:
        logger.info("Closing driver...")
        driver.quit()

if __name__ == "__main__":
    test_gorentals_registration() 