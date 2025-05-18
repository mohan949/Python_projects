from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helpers import *



driver = webdriver.Chrome()

#open website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


time.sleep(3)
try :    

    wait_and_type(driver, (By.XPATH, "//input[@name='username']"), "Admin")
    wait_and_type(driver, (By.XPATH, "//input[@name='password']"), "admin123")
   
    # Get font-related CSS values
    selector = "label.oxd-label"
    expected_properties = {
        "font-family": "Nunito",
        "font-weight": "600",
        "font-size": "12px",
        "padding-top": "0px",
        "padding-left": "0px"
    }
    assert_css_property(driver, selector, expected_properties)
    #click on submit
    wait_and_click(driver, (By.XPATH, "//button[@type='submit']"))

    wait_and_click(driver, (By.XPATH, "//h6[text()='Dashboard']"))

    elements = driver.find_elements(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")
    for _ in elements:
        print('Texts: ',_.text)




except Exception as e :
    print(f'an error as occured: {e}')



finally:
    time.sleep(2)
    driver.quit()