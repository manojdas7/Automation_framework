import os
from pageObjects.HomePage import Homepage
from pageObjects.Login import LoginPage
from time import sleep
from utilities.customLogger import LogGen
from utilities.readproperties import ReadConfig
from utilities import xlutils


class Test_003_LoginUser:
    baseurl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    path = os.path.abspath(os.curdir)+"\\testdata\\nopcommerce.xlsx"

    def test_login_user(self,setup):
        self.logger.info("******** Test 002 Login User Started ********")
        self.rows = xlutils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.logger.info("******** Maximize The Window ********")
        self.hp = Homepage(self.driver)

        for r in range(2, self.rows + 1):

            self.hp.click_login()
            self.login = LoginPage(self.driver)
            self.email_id = xlutils.readData(self.path, "Sheet1", r, 1)
            self.password = xlutils.readData(self.path, "Sheet1", r, 2)
            self.result = xlutils.readData(self.path, "Sheet1", r, 3)
            self.login.enter_email(self.email_id)
            self.login.enter_password(self.password)
            sleep(3)
            self.login.click_login()
            self.error_message = self.login.get_logout_text()

            self.logger.info("****** Login successsfull ******")
            sleep(3)
            if self.result == 'valid':
                lst_status.append("Pass")
                self.login.get_logout_text()
            elif self.result == 'invalid':
                lst_status.append("Fail")
                self.login.get_logout_text()

        self.driver.close()
        self.logger.info("****************** Test__002__loginpage_ddt___ended *************")

        # self.hp.click_login()
        # self.logger.info("******** Click Log In Button ********")
        # self.login_page = LoginPage(self.driver)
        # self.login_page.enter_email("manoj@gmail.com")
        # self.logger.info("******** Enter Email ********")
        # self.login_page.enter_password("1233manoj")
        # self.logger.info("******** Enter Password ********")
        # self.login_page.click_login()
        # self.logger.info("******** Click Log In Button ********")
        #
        # if self.login_page.get_logout_text() == "Log out":
        #     assert "Test case pass: \U0001f601"
        #     self.driver.close()
        #     self.logger.info("******** Check Log Out Button ********")
        # else:
        #     self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"login_user.png")
        #     assert "Test case fail: \U0001F62C"
        # self.logger.info("******** Test 002 Login User Ended ********")
