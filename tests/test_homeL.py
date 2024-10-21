import time
from logging import exception

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
from TestData.homeLData import HomeLData


class TestHome(BaseClass):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    @pytest.mark.taran
    def test_static_dropdown (self,getData):
        log= self.getLogger()
        try:
            TestHome.driver.find_element(By.XPATH,"//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[1]/input[1]").send_keys(getData['Name'])
            TestHome.driver.find_element(By.XPATH,"//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]").send_keys(getData['Password'])
            TestHome.driver.find_element(By.ID,'exampleInputPassword1').send_keys(getData["Password"])
            log.info('successfully filled the fields')
            time.sleep(5)
        except Exception as e:
            log.exception(f"{e}")
        time.sleep(2)
        self.driver.refresh()



    def test_dynamic_dropdown(self):
        TestHome.driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
        TestHome.driver.find_element(By.ID,'autosuggest').send_keys('ind')
        time.sleep(10)
        countries = TestHome.driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")

        for country in countries:
            if country.text == 'India':
                country.click()
                break

        time.sleep(12)
        assert TestHome.driver.find_element(By.ID, 'autosuggest').get_attribute('value') == 'India'

    def test_explicitWait(self):
        TestHome.driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
        #define wait object
        wait = WebDriverWait(TestHome.driver,10)

        #wait for element to display
        dropdown = wait.until(EC.element_to_be_clickable((By.ID,'autosuggest')))

        dropdown.send_keys("Ind")

        #wait for drop down element visibility
        options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"li[class='ui-menu-item'] a")))

        #Itrate the values and perfrom click action

        for option in options:
            if option.text == 'India':
                option.click()
                break
    def test_checkButton(self):

        TestHome.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        options = TestHome.driver.find_elements(By.XPATH,"//input[@type='checkbox']")
        for option in options:
            if option.get_attribute('value')=="option2":
                option.click()
                assert option.is_selected()
                break

        time.sleep(20)
    def test_radioButton(self):

        TestHome.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        radioButton = TestHome.driver.find_elements(By.XPATH,"//input[@class='radioButton']")
        radioButton[2].click()
        assert radioButton[2].is_selected()
        time.sleep(10)

    @pytest.fixture(params=[
        HomeLData.getTestData('testCase1','Sheet2'),
        HomeLData.getTestData('testCase2','Sheet2')])
    def getData(self,request):
        return request.param[0]