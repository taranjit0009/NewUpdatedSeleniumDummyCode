from selenium.webdriver.common.by import By


class CheckOut:
    def __init__(self,driver):
        self.driver = driver


    country= (By.ID,"country")

    def countyInput(self):
       return self.driver.find_element(*CheckOut.country)
