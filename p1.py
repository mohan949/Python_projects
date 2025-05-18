from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set path to your ChromeDriver
driver_path = "C:\\path\\to\\chromedriver.exe"  # Use double backslashes for Windows
#driver = webdriver.Chrome(executable_path=driver_path)
#driver = webdriver.Chrome()
driver = webdriver.Chrome()


# Open a website
driver.get("https://www.google.com")


# Wait for a few seconds
time.sleep(3)
try :    
# Search something
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium with Python")
    search_box.submit()
except Exception as e :
    print(f'an error as occured: {e}')




# Wait and close
time.sleep(2)
driver.quit()
