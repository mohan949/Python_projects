from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Firefox()



# Open a website
driver.get("https://www.saucedemo.com/")


time.sleep(3)
try :    
# Search something
    username = driver.find_element(By.XPATH, "//input[@id='user-name']")
    username.send_keys("problem_user")
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("secret_sauce")
    driver.find_element(By.ID,'login-button').click()

   # //input[@id='login-button']

    time.sleep(5)
    
    # alert = driver.switch_to.alert
    # print('alert', alert.text)
    # alert.accept()

    WebDriverWait(driver, 10).until(
         EC.presence_of_all_elements_located((By.CLASS_NAME,'inventory_item'))
    )

    products =  driver.find_elements(By.CLASS_NAME,'inventory_item')
    print(len(products))
  
    for _ in products:
          _.find_element(By.TAG_NAME,'button').click()
          name =  _.find_element(By.CLASS_NAME,'inventory_item_name').text
          button =  _.find_element(By.TAG_NAME, "button").text
          if button.lower() == 'add to cart':
               print(f"- {name}")

        

except Exception as e :
    print(f'an error as occured INterview: {e}')


  



# Wait and close
time.sleep(2)
driver.quit()



# expetecd - 