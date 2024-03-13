import os
from pageObjects.HomePage import Homepage
from pageObjects.Login import LoginPage
from time import sleep
from utilities.customLogger import LogGen
from utilities.readproperties import ReadConfig


class Test_002_LoginUser:
    baseurl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_login_user(self,setup):
        self.logger.info("******** Test 002 Login User Started ********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.logger.info("******** Maximize The Window ********")
        self.hp = Homepage(self.driver)
        self.hp.click_login()
        self.logger.info("******** Click Log In Button ********")
        self.login_page = LoginPage(self.driver)
        self.login_page.enter_email("manoj@gmail.com")
        self.logger.info("******** Enter Email ********")
        self.login_page.enter_password("1233manoj")
        self.logger.info("******** Enter Password ********")
        self.login_page.click_login()
        self.logger.info("******** Click Log In Button ********")

        if self.login_page.get_logout_text() == "Log out":
            assert "Test case pass: \U0001f601"
            self.driver.close()
            self.logger.info("******** Check Log Out Button ********")
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"login_user.png")
            assert "Test case fail: \U0001F62C"
        self.logger.info("******** Test 002 Login User Ended ********")
