import time

from Utilities.Read_Properties import ReadConfig
from Page_Objects.Login_Page import Loginpage
from TestCases.conftest import setup
from Utilities.CustomLogger import LogGen
from selenium import webdriver
from Utilities import XLUtils

class Test_002_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    path=".//Test_Data/Logindata.xlsx"


    logger = LogGen.loggen()  # Call loggen method using logGen class


    def test_login(self, setup):
        self.logger.info("**************************Test_002_Login************************************`1")
        self.logger.info("***************************Verifying login test*********************************")
        self.driver = setup
        # self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)
        self.lp = Loginpage(self.driver)  # creating object of login page
        self.rows=XLUtils.getRowCount(self.path,'sheet1')
        print("Number of rows in a excel", self.rows)


        lst_status=[]


        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,"sheet1",r,1)
            self.password = XLUtils.readData(self.path, "sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "sheet1", r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.ClickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="pass":
                   self.logger.info("****passed******")
                   self.lp.ClickLogout()
                   lst_status.append("pass")
                elif self.exp=="fail":
                   self.logger.info("****Failed******")
                   self.lp.ClickLogout()
                   lst_status.append("fail")
            elif act_title!=exp_title:
                if self.exp=="pass":
                   self.logger.info("****failed******")
                   self.lp.ClickLogout()
                   lst_status.append("fail")
                elif self.exp=="fail":
                   self.logger.info("****Failed******")
                   self.lp.ClickLogout()
                   lst_status.append("pass")

        if "fail"  not in lst_status:
            self.logger.info("**********Login ddt test passed*************")
            self.driver.close()
            assert True
        else:
            self.logger.info("**********Login ddt test failed*************")
            self.driver.close()
            assert False




        self.logger.info("**********End of  ddt test *************")
        self.logger.info("**********Completed Test_002_Login**************************")