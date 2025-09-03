from selenium.webdriver.common.by import By

class Loginpage:

  textbox_username_id= "Email"
  textbox_password_id = "Password"
  button_Login_xpath = "//button[@class='button-1 login-button']"
  link_logout_Linktext = "Logout"

  def __init__(self,driver):
      self.driver = driver

  def setUserName(self,username):
      # self.driver.find_element_by_id(self.textbox_username_id).clear()
      # self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
      self.driver.find_element(By.ID, self.textbox_username_id).clear()
      self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

  def setPassword(self,password):
      # self.driver.find_element_by_id(self.textbox_password_id).clear()
      # self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
      self.driver.find_element(By.ID, self.textbox_password_id).clear()
      self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

  def ClickLogin(self):
     #self.driver.find_element_by_xpath(self.button_Login_xpath).click()
     self.driver.find_element(By.XPATH, self.button_Login_xpath).click()


  def ClickLogout(self):
     #self.driver.find_element_by_link_text(self.Link_logout_linktext).click()
     self.driver.find_element(By.LINK_TEXT, self.link_logout_Linktext).click()



# class Loginpage:
#     textbox_username_id = "Email"
#     textbox_password_id = "Password"
#     button_Login_xpath = "//button[@class='button-1 login-button']"
#     link_logout_linktext = "Logout"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def setUserName(self, username):
#         self.driver.find_element(By.ID, self.textbox_username_id).clear()
#         self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)
#
#     def setPassword(self, password):
#         self.driver.find_element(By.ID, self.textbox_password_id).clear()
#         self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
#
#     def ClickLogin(self):
#         self.driver.find_element(By.XPATH, self.button_Login_xpath).click()
#
#     def ClickLogout(self):
#         self.driver.find_element(By.LINK_TEXT, self.link_logout_Linktext).click()


