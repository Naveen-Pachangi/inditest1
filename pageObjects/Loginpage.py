import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Loginpage():
    def __init__(self, driver):
        self.driver = driver

    # def _init_(self, driver):
    #     self.driver = driver
    #     self.wait = WebDriverWait(self.driver, 20, poll_frequency=1)

    username_field = (By.ID, "username")  # Update with the actual locator
    password_field = (By.ID, "password")  # Update with the actual locator
    click_login_button_XPATH = (By.XPATH, '//*[@id="login"]/div/div/div/div/div/div/div[2]/div[3]/form/div[4]/button')
    OTP_field = (By.ID, "otp")
    click_Submit_Button_XPATH = (By.XPATH, '//*[@id="login"]/div/div/div/div/div/div/div[2]/div[3]/form/div[3]/button')

    def enter_username(self, Username):
        self.driver.find_element(*Loginpage.username_field).send_keys(Username)

    def enter_password(self, Password):
        self.driver.find_element(*Loginpage.password_field).send_keys(Password)

    def ClickLogin(self):
        self.driver.find_element(*Loginpage.click_login_button_XPATH).click()

    def OTP_read(self, otp):
        self.driver.find_element(*Loginpage.OTP_field).send_keys(otp)

    def SubmitBtn(self):
        self.driver.find_element(*Loginpage.click_Submit_Button_XPATH).click()

# # from configration.config.ini import login data
# class Loginpage():
#     UserName_ID = (By.ID, "username")
#     Password_ID = (By.ID, "password")
#     # LoginButton_XPATH = (By.XPATH, '//*[@id="login"]/div/div/div/div/div/div/div[2]/div[3]/form/div[4]/button')
#     # EnterOTP_ID = (By.ID, "otp")
#     # SubmitButton_ID = (By.ID, '//*[@id="login"]/div/div/div/div/div/div/div[2]/div[3]/form/div[3]/button')
#         # Verify_Login_XPATH = (By.ID, '//*[@id="header"]/div/div[1]/ul/label')
#         # menu_Button_ID = (By.ID, "dropdownBasic2")
#         # LogoutButton_XPATH = (By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[3]/div/a[4]/div/span')
#     def _init_(self,driver):
#         self.driver = driver
#         self.wait = WebDriverWait(self.driver,20, poll_frequency=1)
#
#     def EnterUsername(self,Username):
#         self.wait.until(expected_conditions.presence_of_element_located(self.UserName_ID))
#         self.driver.find_element(*loginpage.UserName_ID).send_keys(Username)
#
#     def EnterPassword(self, Password):
#         self.driver.find_element(*loginpage.Password_ID).send_keys(Password)
#     #
#     # def ClickLogin(self):
#     #     self.driver.find_element(*loginpage.LoginButton_XPATH).click()
#     #
#     # def EnterOTP(self,otp):
#     #     self.wait.until(expected_conditions.presence_of_element_located(self.UserName_ID))
#     #     self.driver.find_element(*loginpage.EnterOTP_ID).send_keys(otp)
#     #
#     # def ClickSubmit(self):
#     #     self.driver.find_element(*loginpage.SubmitButton_ID).click()
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     # # def ClickMenu(self):
#     # #     self.wait.until(expected_conditions.presence_of_element_located(self.LoginButton_XPATH))
#     # #     self.driver.find_element(*loginpage.EnterOTP_ID).click()
#     # #
#     # # def ClickLogout(self):
#     # #     self.driver.find_element(*loginpage.Click_Logout_XPATH).click()
#     # #
#     # # def Title(self):
#     # #     try:
#     # #         self.wait.until(expected_conditions.visibility_of_element_located((self.lp.Click_Menu_XPATH)))
#     # #         title = self.driver.title
#     # #         return True
#     # #     except NoSuchElementException:
#     # #         title = self.driver.title
#     # #     return False
#     # #
#     # # def __init__(self, driver):
#     # #     self.driver = driver
#     # #
#     # # def UserName_ID(self, Username):
#     # #     self.driver.find_element(*loginpage.UserName_ID).send_keys(Username)
#     # #
#     # # def Password_ID(self, Password):
#     # #     self.driver.find_element(*loginpage.Password_ID).send_keys(Password)
#     # #
#     # # def LoginButton_XPATH(self):
#     # #     self.driver.find_element(*loginpage.LoginButton_XPATH).click()
#     # #
#     # # def EnterOTP_ID(self, otp):
#     # #     self.driver.find_element(*loginpage.EnterOTP_ID).send_keys(otp)
#     # #
#     # # def SubmitButton_ID(self):
#     # #     self.driver.find_element(*loginpage.LoginButton_XPATH).click()
#     # # #
#     # # # def Verify_Login_ID(self):
#     # # #     try:
#     # # #         self.driver.find_element(*loginpage.Verify_Login_XPATH)
#     # # #         return "pass"
#     # # #     except:
#     # # #         return "fail"
#     # # #
#     # # # def menu_Button_ID(self):
#     # # #     self.driver.find_element(*loginpage.menu_Button_ID).click()
#     # # #
#     # # # def LogoutButton_XPATH(self):
#     # # #     self.driver.find_element(*loginpage.menu_Button_ID).click()
#
