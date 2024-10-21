from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pageObject.CheckOutPage import CheckOut
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    @pytest.mark.order(1)
    def  test_e2e(self):

        homepage = HomePage(self.driver)
        homepage.shopItem().click()

        # Scanning the all products
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
                break

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        checkout = CheckOut(self.driver)
        checkout.countyInput().send_keys('Ind')
        # wait = WebDriverWait(self.driver,20)
        # wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        message = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you" in message
