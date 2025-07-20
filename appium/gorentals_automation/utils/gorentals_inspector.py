from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import json
import time
from datetime import datetime

class GoRentalsInspector:
    def __init__(self):
        self.driver = None
        
    def connect(self):
        """Connect to the goRentals app"""
        options = UiAutomator2Options()
        options.platform_name = "android"
        options.platform_version = "14"
        options.device_name = "emulator-5554"
        options.automation_name = "UiAutomator2"
        options.app = "/Users/mohanprasad/Documents/goRentals.apk"
        options.auto_grant_permissions = True
        options.app_activity = "com.gorentals.goappprev.MainActivity"
        options.app_package = "com.gorentals.goappprev"
        options.no_reset = True  # Keep app state
        
        self.driver = webdriver.Remote("http://localhost:4723", options=options)
        print("Connected to goRentals app!")
        time.sleep(5)  # Wait for app to load
        
    def inspect_current_screen(self):
        """Inspect and report all elements on current screen"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report = {
            "timestamp": timestamp,
            "activity": self.driver.current_activity,
            "package": self.driver.current_package,
            "elements": []
        }
        
        print(f"\n{'='*60}")
        print(f"SCREEN INSPECTION - {timestamp}")
        print(f"{'='*60}")
        print(f"Current Activity: {report['activity']}")
        print(f"Current Package: {report['package']}")
        print(f"{'='*60}\n")
        
        # Find all elements
        all_elements = self.driver.find_elements(AppiumBy.XPATH, "//*")
        
        print(f"Total elements found: {len(all_elements)}\n")
        
        # Categorize elements
        clickable_count = 0
        editable_count = 0
        
        for i, element in enumerate(all_elements):
            try:
                element_info = {
                    "index": i,
                    "class": element.get_attribute("className"),
                    "text": element.text,
                    "content_desc": element.get_attribute("contentDescription"),
                    "resource_id": element.get_attribute("resourceId"),
                    "clickable": element.get_attribute("clickable") == "true",
                    "enabled": element.is_enabled(),
                    "displayed": element.is_displayed(),
                    "bounds": element.get_attribute("bounds")
                }
                
                # Only add elements that have meaningful content
                if element_info["text"] or element_info["content_desc"] or element_info["resource_id"]:
                    report["elements"].append(element_info)
                    
                    if element_info["clickable"]:
                        clickable_count += 1
                    
                    if element_info["class"] in ["android.widget.EditText", "android.widget.AutoCompleteTextView"]:
                        editable_count += 1
                    
                    # Print important elements
                    if element_info["clickable"] and (element_info["text"] or element_info["content_desc"]):
                        print(f"CLICKABLE ELEMENT #{i}:")
                        print(f"  Text: {element_info['text']}")
                        print(f"  Content Desc: {element_info['content_desc']}")
                        print(f"  Class: {element_info['class']}")
                        print(f"  Resource ID: {element_info['resource_id']}")
                        print()
                    
                    elif element_info["class"] in ["android.widget.EditText", "android.widget.AutoCompleteTextView"]:
                        print(f"INPUT FIELD #{i}:")
                        print(f"  Hint/Text: {element_info['text']}")
                        print(f"  Resource ID: {element_info['resource_id']}")
                        print(f"  Class: {element_info['class']}")
                        print()
                        
            except Exception as e:
                pass
        
        print(f"\nSUMMARY:")
        print(f"  - Clickable elements: {clickable_count}")
        print(f"  - Input fields: {editable_count}")
        print(f"  - Total meaningful elements: {len(report['elements'])}")
        
        # Ensure test_outputs directory exists
        import os
        os.makedirs("test_outputs", exist_ok=True)
        
        # Save detailed report
        report_filename = f"test_outputs/gorentals_inspection_{timestamp}.json"
        with open(report_filename, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\nDetailed report saved to: {report_filename}")
        
        # Save page source
        source_filename = f"test_outputs/gorentals_source_{timestamp}.xml"
        with open(source_filename, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        print(f"Page source saved to: {source_filename}")
        
        # Take screenshot
        screenshot_filename = f"test_outputs/gorentals_screen_{timestamp}.png"
        self.driver.save_screenshot(screenshot_filename)
        print(f"Screenshot saved to: {screenshot_filename}")
        
        return report
    
    def find_elements_by_text(self, text):
        """Find all elements containing specific text"""
        print(f"\nSearching for elements containing text: '{text}'")
        
        # Try different methods
        methods = [
            ("Text match", f'new UiSelector().text("{text}")'),
            ("Text contains", f'new UiSelector().textContains("{text}")'),
            ("Content description", f'new UiSelector().description("{text}")'),
            ("Content description contains", f'new UiSelector().descriptionContains("{text}")')
        ]
        
        found_elements = []
        
        for method_name, selector in methods:
            try:
                elements = self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, selector)
                if elements:
                    print(f"\n{method_name}: Found {len(elements)} element(s)")
                    for elem in elements:
                        elem_info = {
                            "method": method_name,
                            "text": elem.text,
                            "class": elem.get_attribute("className"),
                            "clickable": elem.get_attribute("clickable") == "true"
                        }
                        found_elements.append(elem_info)
                        print(f"  - {elem_info}")
            except:
                pass
        
        return found_elements
    
    def interactive_mode(self):
        """Run in interactive mode for exploration"""
        print("\n" + "="*60)
        print("INTERACTIVE MODE - Type 'help' for commands")
        print("="*60)
        
        while True:
            try:
                command = input("\n> ").strip().lower()
                
                if command == "help":
                    print("\nAvailable commands:")
                    print("  inspect    - Inspect current screen")
                    print("  find TEXT  - Find elements by text")
                    print("  click TEXT - Click element with text")
                    print("  swipe up   - Swipe up")
                    print("  swipe down - Swipe down")
                    print("  back       - Press back button")
                    print("  home       - Press home button")
                    print("  screenshot - Take screenshot")
                    print("  source     - Save page source")
                    print("  quit       - Exit")
                
                elif command == "inspect":
                    self.inspect_current_screen()
                
                elif command.startswith("find "):
                    search_text = command[5:]
                    self.find_elements_by_text(search_text)
                
                elif command.startswith("click "):
                    click_text = command[6:]
                    try:
                        element = self.driver.find_element(
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            f'new UiSelector().textContains("{click_text}")'
                        )
                        element.click()
                        print(f"Clicked: {click_text}")
                        time.sleep(1)
                    except Exception as e:
                        print(f"Could not click '{click_text}': {e}")
                
                elif command == "swipe up":
                    size = self.driver.get_window_size()
                    self.driver.swipe(
                        size['width']//2, size['height']*0.8,
                        size['width']//2, size['height']*0.2, 500
                    )
                    print("Swiped up")
                
                elif command == "swipe down":
                    size = self.driver.get_window_size()
                    self.driver.swipe(
                        size['width']//2, size['height']*0.2,
                        size['width']//2, size['height']*0.8, 500
                    )
                    print("Swiped down")
                
                elif command == "back":
                    self.driver.press_keycode(4)
                    print("Pressed back button")
                
                elif command == "home":
                    self.driver.press_keycode(3)
                    print("Pressed home button")
                
                elif command == "screenshot":
                    filename = f"test_outputs/screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    self.driver.save_screenshot(filename)
                    print(f"Screenshot saved: {filename}")
                
                elif command == "source":
                    filename = f"test_outputs/source_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xml"
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(self.driver.page_source)
                    print(f"Page source saved: {filename}")
                
                elif command == "quit":
                    break
                
                else:
                    print("Unknown command. Type 'help' for available commands.")
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")
        
        print("\nExiting interactive mode...")
    
    def cleanup(self):
        """Clean up resources"""
        if self.driver:
            self.driver.quit()

# Main execution
if __name__ == "__main__":
    inspector = GoRentalsInspector()
    
    try:
        inspector.connect()
        
        # Perform initial inspection
        inspector.inspect_current_screen()
        
        # Enter interactive mode
        inspector.interactive_mode()
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        inspector.cleanup() 