import time

import pytest
from selenium import webdriver
from pageObjects.Loginpage import Loginpage
from utilites.ReadconfigFile import ReadconfigClass
from utilites.logger import LogGenerator


class TestLoginPage:
    # Class-level configuration and logging setup
    login_url = ReadconfigClass.getURL()
    username = ReadconfigClass.getUsername()
    password = ReadconfigClass.getPassword()
    Read_OTP = ReadconfigClass.getotp()

    logs = LogGenerator.loggen()

    def test_page_title_001(self, setup):
        self.logs.info("test_page_title_001 is started")
        self.driver = setup
        self.logs.info("Opening Browser")
        self.lp = Loginpage(self.driver)
        self.driver.get(self.login_url)
        self.logs.info("Going to Url -->" + self.login_url)  ##URL

        expected_title = "IndiConnect-Branchless Banking"
        if self.driver.title == expected_title:
            self.logs.info(f"Page title is correct: {self.driver.title}")
            assert True

            # self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\Indiconnect\\screenshots\\test_pass_003.png")
        else:
            self.logs.error(f"Page title is incorrect: {self.driver.title}")
            assert False
            # driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\Indiconnect\\screenshots\\test_pass_003.png")

        self.logs.info("Test case test_user_login_001 executed")
        time.sleep(3)

    def test_Login_002(self, setup):
        self.logs.info("Test_Login_002 is started")
        self.driver = setup

        self.logs.info("opening Browser")
        self.lp = Loginpage(self.driver)
        self.driver.get(self.login_url)
        self.logs.info("Going to URL --" + str(self.login_url))

        # Perform login actions
        self.logs.info("Entering username")
        self.lp.enter_username(self.username)

        self.logs.info("Entering password")
        self.lp.enter_password(self.password)

        self.logs.info("click login button")
        self.lp.ClickLogin()

        self.logs.info("Enter OTP ")
        self.lp.OTP_read(self.Read_OTP)

        self.logs.info("Clicking on submit button")
        self.lp.SubmitBtn()

        time.sleep(3)

        # self.logs.info("Submitting Username and password")
        # login_page.Submit_button()
        #
        # self.logs.info("Entering OTP"+ self.Read_OTP)
        # login_page.OTP_field()
        #
        # self.logs.info("Submitting otp ")
        # login_page.SubmitBtn()
        #
        #

#         def test_login_002(self, setup):
#             self.log.info("test_login_002 is started")
#             self.driver = setup
#             self.log.info("Opening Browser")
#             self.lp = LoginPage(self.driver)
#             self.driver.get(self.url)
#             self.log.info("Going to Url -->" + str(self.url))
#             self.lp = LoginPage(self.driver)
#             time.sleep(2)
#             self.lp.EnterEmail(self.email)
#             self.log.info("Entering Email-->" + str(self.email))
#             self.lp.EnterPassword(self.password)
#             self.log.info("Entering Password-->" + self.password)
#             self.lp.ClickLogin()
#             self.log.info("Clicking Login")
#             # time.sleep(2)
#             # wait = WebDriverWait(self.driver, 15, poll_frequency=1)
#             # try:
#             #     wait.until(expected_conditions.visibility_of_element_located((self.lp.Click_Menu_XPATH)))
#             #     title = self.driver.title
#             # except NoSuchElementException:
#             #     title = self.driver.title
#
#
#
#         #
#     # @pytest.fixture
#     # def setup(self):
#     #     # Setup the WebDriver and provide a fixture for tests
#     #     driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser
#     #     driver.implicitly_wait(10)
#     #     yield driver
#     #     driver.quit()
#     #
#     # def test_user_login_001(self, setup):
#     #     self.logs.info("Starting test_user_login_001")
#     #     driver = setup
#     #
#     #     # Navigate to the login URL
#     #     driver.get(self.login_url)
#     #     self.logs.info(f"Navigated to URL: {self.login_url}")
#     #
#     #     # Initialize the login page object
#     #     login_page = Loginpage(driver)
#     #
#     #     # Perform login actions
#     #     self.logs.info("Entering username")
#     #     login_page.enter_username(self.username)
#     #
#     #     self.logs.info("Entering password")
#     #     login_page.enter_password(self.password)
#     #     time.sleep(3)
#     #
#     #     self.logs.info("Submitting Username and password")
#     #     login_page.Submit_button()
#     #
#     #     self.logs.info("Entering OTP"+ self.Read_OTP)
#     #     login_page.OTP_field()
#     #
#     #     self.logs.info("Submitting otp ")
#     #     login_page.SubmitBtn()
#
#
#         #
#         # self.logs.info("Entering password")
#         # login_page.enter_password(self.password)
#         # time.sleep(3)
#
#         # Validate the page title
#
#
# # import pytest
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from pageObjects.Loginpage import loginpage
# # from utilites.ReadconfigFile import ReadconfigClass
# # from utilites.logger import LogGenerator
# #
# #
# # class Test_Loginpage:
# #     Login_url = ReadconfigClass.getURL()
# #     username = ReadconfigClass.getUsername()
# #     Password = ReadconfigClass.getPassword()
# #     # Login_Button = ReadconfigClass.getLogin_button()
# #     # Read_OTP = ReadconfigClass.getotp()
# #     # SubmitButton = ReadconfigClass.getSbmitButton()
# #     logs = LogGenerator.loggen()
# #
# #     def test_user_login_001(self, setup):
# #         self.logs.info("test_user_login_001 started")
# #         self.driver = setup
# #
# #         self.driver.get(self.Login_url)
# #         self.logs.info("Going to URL -->" + self.Login_url)
# #
# #         self.logs.info("Opening browser")  ##opening browser
# #         self.lp = loginpage()  ##init loginpage as lp
# #
# #         # self.logs.info("opening URL")
# #         # self.lp.
# #         # self.lp.UserName_ID(self.Login_url)
# #
# #         self.logs.info("Entering username")
# #         self.lp.UserName_ID(self.username)
# #
# #         self.logs.info("Entering password")
# #         self.lp.Password_ID(self.Password)
# #
# #
# #
# #         if self.driver.title == "IndiConnect-Branchless Banking":
# #             self.logs.info("page title --" + self.driver.title)
# #             assert True
# #             self.driver.save_screenshot(
# #                 "C:\\Users\\admin\\PycharmProjects\\Indiconnect\\screenshots\\test_pass_001.PNG")
# #
# #         else:
# #             self.log.info("page title --" + self.driver.title)
# #             assert False
# #             self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\Indiconnect\\screenshots\\test_fail_001.PNG")
# #
# #
# # #
# # #         self.log.info("Clicking login button")
# # #         self.lg.click_login_button()
# # #
# # #         self.log.info("Entering OTP")
# # #         self.lg.enter_otp(self.otp)
# # #
# # #         self.log.info("Submitting OTP")
# # #         self.lg.click_submit_button()
# # #
# # #         if self.lg.verify_login_success():
# # #             self.log.info("Taking screenshot of successful login")
# # #             self.driver.save_screenshot(".\\screenshots\\Login_001_pass.PNG")
# # #             self.log.info("Test case for login passed")
# # #             assert True
# # #         else:
# # #             self.log.info("Taking screenshot of failed login")
# # #             self.driver.save_screenshot(".\\screenshots\\Login_001_fail.PNG")
# # #             self.log.info("Test case for login failed")
# # #             assert False
# # #
# # #         self.log.info("Test case for login executed\n")
# # #
# # # #     # def test_userlogin_001(self,setup):
# # #     #     self.log.info("userlogin_001 started ")
# # #     #     self.log.info("opening browser")
# # #     #
# # #     #     self.driver = setup
# # #     #     self.lg = loginpage(self.driver)
# # #     #
# # #     #     self.log.info("username entered" + self.Username)
# # #     #     self.lg.UserName_ID = (By.ID, "username")
# # #     #
# # #     #     self.log.info("enter password" + self.password)
# # #     #     self.lg.Password_ID = (By.ID, "password")
# # #     #
# # #     #     self.log.info("enter LoginButton")
# # #     #     self.lg.LoginButton_XPATH()
# # #     #
# # #     #     self.log.info("enter otp" + self.otp)
# # #     #     self.lg.EnterOTP_ID = (By.ID, "otp")
# # #     #
# # #     #     self.log.info("submiting otp")
# # #     #     self.lg.SubmitButton_ID()
# # #     #
# # #     #     if self.lg.Verify_Login_XPATH() == "Pass":
# # #     #         self.log.info("taking sceenshot")
# # #     #         self.driver.save_screenshot(".\\screenshots\\Login_001_pass.PNG")
# # #     #         self.log.info("testcase of login is pass")
# # #     #         assert True
# # #     #     else:
# # #     #         self.log.info("taking sceenshot")
# # #     #         self.driver.save_screenshot(".\\screenshots\\Login_001_fail.PNG")
# # #     #         self.log.info("testcase of login is fail")
# # #     #         assert False
# # #     #     self.log.info("testcase of login and logout page executed \n")
# # #     #
# # #     #
# # #     #
# # #     #
# # #     #
# # #     #
# # #     #
# # #
# # # # class test_001:
# # # #     logs = LogGenerator.loggen()
# # # #     username = ReadconfigClass.getUsername()
# # # #     Password = ReadconfigClass.getPassword()
# # # #
# # # #     def test_pageTitle_0001(self,setup):
# # # #         self.log.info("userlogin strated")
# # # #         self.log.info("opening broweser")
# # # #
# # # #         self.driver = setup
# # # #         self.lg = loginpage(self.driver)
# # # #     def test_userlogin_001(self,setup):
# # # #         self.log.info("userlogin_001 started ")
# # # #         self.log.info("opening browser")
# # # #
# # # #         self.driver = setup
# # # #         self.lg = loginpage(self.driver)
