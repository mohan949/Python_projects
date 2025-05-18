

from selenium import webdriver

class Booking(webdriver.Chrome):
    def __init__(self,  webdriver.Chrome()):
        self.driver_path = driver_path
        super(Booking, self).__init__(executable_path=self.driver_path)
        self.implicitly_wait(15)
        self.maximize_window()