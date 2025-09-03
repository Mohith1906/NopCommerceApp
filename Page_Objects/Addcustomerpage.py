import time

import self
from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AddCustomerPage:

    link_customer_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_page_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_addnew_xpath="//a[@class='btn btn-primary']"

    txt_Email_xpath="//input[@id='Email']"
    txt_Password_xpath="//input[@id='Password']"
    txt_FirstName_xpath="//input[@id='FirstName']"
    txt_LastName_xpath="//input[@id='LastName']"

    rb_Gender_male_xpath="//input[@id='Gender_Male']"
    rb_Gender_female_xpath="//input[@id='Gender_Female']"

    txt_CompanyName_xpath="//input[@id='Company']"
    txt_Customerroles_xpath="//span[@aria-expanded='true']//ul[@class='select2-selection__rendered']"
    txt_CRregistered_xpath="//li[@title='Registered']"
    txt_CRAdministrators_xpath="//li[@title='Administrators']"
    txt_CRForums_xpath="//li[@title='Forum Moderators']"
    txt_CRvendor_xpath="//li[@title='Vendors']"
    txt_CRGuests_xpath="//li[@title='Guests']"
    cb_istax_xpath="//input[@id='IsTaxExempt']"
    txt_newsletter_xpath="//span[@aria-expanded='true']//input[@role='searchbox']"
    txt_managervendor_xpath="//select[@id='VendorId']"
    cb_active_xpath="//input[@id='Active']"
    cb_customermustchangepassword_xpath="//input[@id='MustChangePassword']"
    txt_admincontent_xpath="//textarea[@id='AdminComment']"
    btn_save_xpath="//button[@name='save']"


    # def __init__(self, driver):
    #     self.driver = driver
    # self.driver.implicitly_wait(10)

    #
    # def click_customer(self):
    #     self.driver.get(self.link_customer_xpath).click()
    # def click_customerpage(self):
    #
    #     self.driver.get(self.link_customer_page_xpath).click()
    # def clickaddnew(self):
    #     self.driver.get(self.btn_addnew_xpath).click()
    #
    # def setemail(self,email):
    #     self.driver.find_element_by_xpath(self.txt_Email_xpath).sendkeys(email)
    #
    # def setpassword(self,password):
    #     self.driver.find_element_by_xpath(self.txt_Password_xpath).sendkeys(password)
    #
    # def setfirstname(self,fname):
    #     self.driver.find_element_by_xpath(self.txt_FirstName_xpath).sendkeys(fname)
    #
    # def setlastname(self,lname):
    #     self.driver.find_element_by_xpath(self.txt_LastName_xpath).sendkeys(lname)
    #
    # def setcustomerroles(self,role):
    #     self.driver.find_element_by_xpath(self.cb_istax_xpath).click()
    #     time.sleep(3)
    #     if role == "Registered":
    #         self.listitem=self.driver.find_element_by_xpath(self.txt_CRregistered_xpath)
    #     elif role == "Administrators":
    #         self.listitem=self.driver.find_element_by_xpath(self.txt_CRAdministrators_xpath)
    #     elif role == "Guests":
    #         #here user can be registered ot guest, only one
    #         time.sleep(4)
    #         self.driver.find_element_by_xpath("//li[@title='Registered']//span[@role='presentation'][normalize-space()='×']").click()
    #         self.listitem = self.driver.find_element_by_xpath(self.txt_CRGuests_xpath)
    #     elif role == "Forum Moderators":
    #         self.listitem=self.driver.find_element_by_xpath(self.txt_CRForums_xpath)
    #     elif role == "Vendors":
    #         self.listitem=self.driver.find_element_by_xpath(self.txt_CRvendor_xpath)
    #     else:
    #         self.listitem=self.driver.find_element_by_xpath(self.txt_CRGuests_xpath)
    #     time.sleep(3)
    #     #self.listitem.click()  #as the click method not works on listitem
    #     self.driver.execute_script("arguments[0].click();", self.listitem)
    #
    # def setmanagervendors(self,value):
    #     drp=select(self.driver.find_element_by_xpath(self.txt_managervendor_xpath))
    #     drp.select_by_visible_text(value)
    #
    # def setGender(self,gender):
    #     if gender == "Male":
    #         self.driver.find_element_by_xpath(self.rb_Gender_male_xpath).click()
    #     elif gender == "Female":
    #         self.driver.find_element_by_xpath(self.rb_Gender_female_xpath).click()
    #     else:
    #         self.driver.find_element_by_xpath(self.rb_Gender_male_xpath).click()
    #
    # def setnewsletter(self,newsletter):
    #     self.driver.find_element_by_xpath(self.txt_newsletter_xpath)
    #     self.driver.find_element_by_xpath("//li[@title='nopCommerce admin demo store']")
    #     self.driver.execute_script("arguments[0].click();", self.listitem)
    #     time.sleep(3)
    #
    # def setcompanyname(self,companyname):
    #     self.driver.find_element_by_xpath(self.txt_CompanyName_xpath).send_keys(companyname)
    #
    # def settax(self):
    #     self.driver.find_element_by_xpath(self.cb_istax_xpath).click()
    #
    # def setactive(self):
    #     self.driver.find_element_by_xpath(self.cb_active_xpath).click()
    #
    # def setcustomermustchangepassword(self):
    #     self.driver.find_element_by_xpath(self.cb_customermustchangepassword_xpath).click()
    #
    # def setadmincontent(self,admincontent):
    #     self.driver.find_element_by_xpath(self.txt_admincontent_xpath).send_keys(admincontent)
    #
    # def clicksavebtn(self):
    #     self.driver.find_element_by_xpath(self.btn_save_xpath).click()

    def __init__(self, driver):
        self.driver = driver
        # self.driver.implicitly_wait(10)

    def click_customer(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.link_customer_page_xpath))).click()
        self.driver.find_element(By.XPATH, self.link_customer_page_xpath).click()
        self.driver.find_element(By.XPATH,self.link_customer_xpath).click()

    def click_customerpage(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.link_customer_page_xpath))).click()
        self.driver.find_element(By.XPATH,self.link_customer_page_xpath).click()

    def clickaddnew(self):
        self.driver.find_element(By.XPATH,self.btn_addnew_xpath).click()

    def setemail(self,email):
        self.driver.find_element(By.XPATH,self.txt_Email_xpath).send_keys(email)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.txt_Password_xpath).send_keys(password)

    def setfirstname(self,fname):
        self.driver.find_element(By.XPATH,self.txt_FirstName_xpath).send_keys(fname)

    def setlastname(self,lname):
        self.driver.find_element(By.XPATH,self.txt_LastName_xpath).send_keys(lname)

    def setcustomerroles(self,role):
        self.driver.find_element(By.XPATH,self.cb_istax_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem=self.driver.find_element(By.XPATH,self.txt_CRregistered_xpath)
        elif role == "Administrators":
            self.listitem=self.driver.find_element(By.XPATH,self.txt_CRAdministrators_xpath)
        elif role == "Guests":
            #here user can be registered ot guest, only one
            time.sleep(4)
            self.driver.find_element(By.XPATH,"//li[@title='Registered']//span[@role='presentation'][normalize-space()='×']").click()
            self.listitem = self.driver.find_element(By.XPATH,self.txt_CRGuests_xpath)
        elif role == "Forum Moderators":
            self.listitem=self.driver.find_element(By.XPATH,self.txt_CRForums_xpath)
        elif role == "Vendors":
            self.listitem=self.driver.find_element(By.XPATH,self.txt_CRvendor_xpath)
        else:
            self.listitem=self.driver.find_element(By.XPATH,self.txt_CRGuests_xpath)
        time.sleep(3)
        #self.listitem.click()  #as the click method not works on listitem
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setmanagervendors(self,value):
        drp=select(self.driver.find_element(By.XPATH,self.txt_managervendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH,self.rb_Gender_male_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH,self.rb_Gender_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.rb_Gender_male_xpath).click()

    def setnewsletter(self, newsletter):
        element = self.driver.find_element(By.XPATH, self.txt_newsletter_xpath)
        element.click()
        listitem = self.driver.find_element(By.XPATH, "//li[@title='nopCommerce admin demo store']")
        self.driver.execute_script("arguments[0].click();", listitem)
        time.sleep(3)

    # def setnewsletter(self,newsletter):
    #     self.driver.find_element(By.XPATH,self.txt_newsletter_xpath)
    #     self.driver.find_element(By.XPATH,"//li[@title='nopCommerce admin demo store']")
    #     self.driver.execute_script("arguments[0].click();", self.listitem)
    #     time.sleep(3)

    def setcompanyname(self,companyname):
        self.driver.find_element(By.XPATH,self.txt_CompanyName_xpath).send_keys(companyname)

    def settax(self):
        self.driver.find_element(By.XPATH,self.cb_istax_xpath).click()

    def setactive(self):
        self.driver.find_element(By.XPATH,self.cb_active_xpath).click()

    def setcustomermustchangepassword(self):
        self.driver.find_element(By.XPATH,self.cb_customermustchangepassword_xpath).click()

    def setadmincontent(self,admincontent):
        self.driver.find_element(By.XPATH,self.txt_admincontent_xpath).send_keys(admincontent)

    def clicksavebtn(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()



