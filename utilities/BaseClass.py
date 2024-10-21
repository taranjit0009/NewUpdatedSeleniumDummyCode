import inspect
import time
import logging
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from TestData import homeLData


#@pytest.mark.usefixtures('setup')
class BaseClass:

    def verifyLinkPresence(self,text):

        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.LINK_TEXT,text)))

    #We are passing params as tuples
    # @pytest.fixture(scope="class",params=[("Taranjit","taranjit@tata.com","pass@3212"),("Rahu","abcd@tata.com",'password233')])
    # def forData(self,request):
    #     return request.param


    #We are passing params by dictionary
    # @pytest.fixture(scope="class",params=homeLData.HomeLData.test_homeL_page_data)
    # def forData(self, request):
    #     return request.param



    def getLogger(self):

        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        filehandler = logging.FileHandler('logfile.log')

        formatter  = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)

        return logger