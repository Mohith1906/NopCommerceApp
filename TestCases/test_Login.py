from Utilities.Read_Properties import ReadConfig
from Page_Objects.Login_Page import Loginpage
from TestCases.conftest import setup
from Utilities.CustomLogger import LogGen
from selenium import webdriver

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Call loggen method using logGen class

    def test_homepagetitle(self, setup):
        self.logger.info("***************************Test_001_Login*********************************")
        self.logger.info("***************************Verifying home page title*********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info( "***************************Home page title test is passed*********************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepagetitle.png")
            self.driver.close()
            self.logger.error("***************************Home page title test is Failed*********************************")
            assert False


    def test_login(self, setup):
        self.logger.info("***************************Verifying login test*********************************")
        self.driver = setup
        # self.driver.implicitly_wait(10)
        self.driver.get(self.baseUrl)
        self.lp = Loginpage(self.driver)  # creating object of login page
        self.lp.setUserName(self.username)  # By using lp object, we are calling the action method
        self.lp.setPassword(self.password)  # By using lp object, we are calling the action method
        self.lp.ClickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            print("Actual title:", act_title)
            assert True
            self.logger.info("***************************Login test is passed*********************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepagetitle.png")
            self.driver.close()
            self.logger.error("***************************Login title test is Failed*********************************")
            assert False
        #By using lp object, we are calling the action method
            # self.lp.ClickLogout()    #By using lp object, we are calling the action method


