from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GoRentalsAutomation:
    def __init__(self):
        self.driver = None
        self.wait = None
        
    def setup_driver(self):
        """Initialize Appium driver with goRentals app capabilities"""
        options = UiAutomator2Options()
        options.platform_name = "android"
        options.platform_version = "14"
        options.device_name = "emulator-5554"
        options.automation_name = "UiAutomator2"
        options.app = "/Users/mohanprasad/Documents/goRentals.apk"
        options.auto_grant_permissions = True
        options.app_activity = "com.gorentals.goappprev.MainActivity"
        options.app_package = "com.gorentals.goappprev"
        options.new_command_timeout = 300
        options.no_reset = False
        
        try:
            self.driver = webdriver.Remote("http://localhost:4723", options=options)
            self.wait = WebDriverWait(self.driver, 20)
            logger.info("Successfully connected to goRentals app!")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to app: {e}")
            return False
    
    def find_element_safe(self, locator_type, locator_value, timeout=10):
        """Safely find an element with timeout"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((locator_type, locator_value))
            )
            return element
        except TimeoutException:
            logger.warning(f"Element not found: {locator_type} = {locator_value}")
            return None
    
    def click_element_safe(self, locator_type, locator_value, timeout=10):
        """Safely click an element"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            element.click()
            logger.info(f"Clicked element: {locator_value}")
            return True
        except Exception as e:
            logger.warning(f"Could not click element: {locator_value} - {e}")
            return False
    
    def enter_text(self, locator_type, locator_value, text, timeout=10):
        """Enter text into an input field"""
        try:
            element = self.find_element_safe(locator_type, locator_value, timeout)
            if element:
                element.clear()
                element.send_keys(text)
                logger.info(f"Entered text: {text}")
                return True
        except Exception as e:
            logger.error(f"Could not enter text: {e}")
        return False
    
    def swipe_up(self, duration=500):
        """Swipe up on the screen"""
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2
        
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
        logger.info("Swiped up")
    
    def swipe_down(self, duration=500):
        """Swipe down on the screen"""
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] * 0.2
        end_y = size['height'] * 0.8
        
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
        logger.info("Swiped down")
    
    def scroll_to_element(self, text):
        """Scroll to find element with specific text"""
        try:
            element = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(text("{text}"))'
            )
            logger.info(f"Scrolled to element with text: {text}")
            return element
        except Exception as e:
            logger.warning(f"Could not scroll to element: {text} - {e}")
            return None
    
    def take_screenshot(self, filename):
        """Take a screenshot with timestamp"""
        try:
            # Ensure test_outputs directory exists
            import os
            os.makedirs("test_outputs", exist_ok=True)
            
            # Add test_outputs prefix if not already present
            if not filename.startswith("test_outputs/"):
                filename = f"test_outputs/{filename}"
            
            self.driver.save_screenshot(filename)
            logger.info(f"Screenshot saved: {filename}")
        except Exception as e:
            logger.error(f"Could not take screenshot: {e}")
    
    def get_page_info(self):
        """Get current page information for debugging"""
        info = {
            "activity": self.driver.current_activity,
            "package": self.driver.current_package,
            "window_size": self.driver.get_window_size()
        }
        logger.info(f"Page info: {info}")
        return info
    
    # Test Scenarios
    
    def handle_onboarding(self):
        """Handle initial app onboarding/permissions"""
        logger.info("=== Handling Onboarding ===")
        
        # Common onboarding elements
        onboarding_buttons = ["Skip", "Next", "Get Started", "Allow", "Continue"]
        
        for button_text in onboarding_buttons:
            if self.click_element_safe(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().textContains("{button_text}")'
            ):
                time.sleep(1)  # Wait between clicks
        
        self.take_screenshot("onboarding_complete.png")
    
    def test_login_flow(self, username=None, password=None):
        """Test login functionality"""
        logger.info("=== Testing Login Flow ===")
        
        # Look for login button
        login_clicked = self.click_element_safe(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("Login")'
        ) or self.click_element_safe(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("Sign In")'
        )
        
        if login_clicked:
            time.sleep(2)
            
            # Try to find username/email field
            if username:
                self.enter_text(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)',
                    username
                )
            
            # Try to find password field
            if password:
                self.enter_text(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)',
                    password
                )
            
            self.take_screenshot("login_filled.png")
            
            # Click login/submit button
            self.click_element_safe(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().textMatches("Login|Sign In|Submit")'
            )
            
            time.sleep(3)
            self.take_screenshot("login_result.png")
    
    def test_search_functionality(self, search_term="Car"):
        """Test search feature"""
        logger.info("=== Testing Search Functionality ===")
        
        # Look for search field
        search_found = self.click_element_safe(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("Search")'
        ) or self.click_element_safe(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.EditText").textContains("Search")'
        )
        
        if search_found:
            time.sleep(1)
            # Enter search term
            self.enter_text(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").focused(true)',
                search_term
            )
            
            # Press search/enter
            self.driver.press_keycode(66)  # Enter key
            
            time.sleep(2)
            self.take_screenshot("search_results.png")
    
    def explore_app_navigation(self):
        """Explore main app navigation"""
        logger.info("=== Exploring App Navigation ===")
        
        # Common navigation items in rental apps
        nav_items = ["Home", "Search", "Categories", "Profile", "Account", "Menu", "Rentals"]
        
        for item in nav_items:
            if self.click_element_safe(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().textContains("{item}")',
                timeout=5
            ):
                time.sleep(2)
                self.take_screenshot(f"nav_{item.lower()}.png")
                self.get_page_info()
    
    def cleanup(self):
        """Clean up and close driver"""
        if self.driver:
            logger.info("Closing driver...")
            self.driver.quit()

# Main execution
if __name__ == "__main__":
    automation = GoRentalsAutomation()
    
    try:
        # Setup driver
        if not automation.setup_driver():
            logger.error("Failed to setup driver. Exiting.")
            exit(1)
        
        # Wait for app to load
        time.sleep(5)
        
        # Get initial page info
        automation.get_page_info()
        automation.take_screenshot("initial_screen.png")
        
        # Save page source for analysis
        with open("test_outputs/gorentals_page_structure.xml", "w", encoding="utf-8") as f:
            f.write(automation.driver.page_source)
        logger.info("Page source saved to test_outputs/gorentals_page_structure.xml")
        
        # Run test scenarios
        automation.handle_onboarding()
        
        # Uncomment and customize these based on your app
        # automation.test_login_flow(username="test@example.com", password="testpass")
        # automation.test_search_functionality("Bike")
        # automation.explore_app_navigation()
        
        # Example: Find all clickable elements on current screen
        clickable_elements = automation.driver.find_elements(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().clickable(true)'
        )
        logger.info(f"Found {len(clickable_elements)} clickable elements on current screen")
        
        # Example: Find all text views
        text_elements = automation.driver.find_elements(
            AppiumBy.CLASS_NAME,
            "android.widget.TextView"
        )
        logger.info(f"Found {len(text_elements)} text elements")
        
        for i, element in enumerate(text_elements[:10]):  # First 10 text elements
            try:
                text = element.text
                if text:
                    logger.info(f"Text {i}: {text}")
            except:
                pass
        
        logger.info("\n=== Automation completed successfully! ===")
        
    except Exception as e:
        logger.error(f"Error during automation: {e}")
        if automation.driver:
            automation.take_screenshot("error_screenshot.png")
    
    finally:
        automation.cleanup() 