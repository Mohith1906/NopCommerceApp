import pytest
import time

from selenium.webdriver.common.by import By

from Page_Objects.Login_Page import Loginpage
from Page_Objects.Addcustomerpage import AddCustomerPage
from Utilities.Read_Properties import ReadConfig
from Utilities.CustomLogger import LogGen
import string
import random


# def random_generator(size=8, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Test_003_Addcustomer():
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addcustomer(self,setup):
        self.logger.info("*******************************Test_003_Addcustomer.test_addcustomer****************************************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()


        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)  # By using lp object, we are calling the action method
        self.lp.setPassword(self.password)  # By using lp object, we are calling the action method
        self.lp.ClickLogin()
        self.logger.info("***************login succesful*****************")

        self.logger.info("****************Starting add customer test**********************")


        self.addcust = AddCustomerPage(self.driver)  #creating object for page object class AddCustomerPage
        self.addcust.click_customer()
        self.addcust.click_customerpage()
        self.addcust.clickaddnew()

        self.logger.info("****************Providing customer information******************************")


        self.email = random_generator() + "@gmail.com"
        self.addcust.setemail(self.email)
        self.addcust.setpassword("test123")
        self.addcust.setcustomerroles("Guests")
        self.addcust.setmanagervendors("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setfirstname("Pavan")
        self.addcust.setlastname("Kumar")
        self.addcust.setcompanyname("busyQA")
        self.addcust.setnewsletter()
        self.addcust.settax()
        self.addcust.setactive()
        self.addcust.setcustomermustchangepassword()
        self.addcust.setadmincontent("This is for testing........")
        self.addcust.clicksavebtn()

        self.logger.info("******************************saving customer information******************************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text #body is given to dispalay eveything from the page

        print(self.msg)

        if "customer has been added successfully" in self.msg:
            assert True == True
            self.logger.info("*****************AddCustomer Test Passed*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "AddCustomer.png")
            self.logger.error("****************AddCustomer Test Failed********************")
            assert False == True


        self.driver.close()
        self.logger.info(("*********Ending add customer test*************************"))