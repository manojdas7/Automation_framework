import os
from pageObjects.HomePage import Homepage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from time import sleep
from utilities import random_string
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_AccountReg:
    baseurl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_account_reg(self,setup):
        self.logger.info("******** Test 001 Account Registration Started ********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.logger.info("******** Maximize The Window ********")
        self.hp = Homepage(self.driver)
        self.hp.click_register()
        self.logger.info("******** Click Register Button ********")
        self.reg_page = AccountRegistrationPage(self.driver)
        self.reg_page.set_gender()
        self.logger.info("******** select gender ********")
        self.reg_page.set_firstname("manoj")
        self.reg_page.set_lastname("das")
        self.logger.info("******** Enter First and Last Name ********")
        sleep(10)
        # self.reg_page.set_day_ofbirth("3")
        # self.reg_page.set_day_ofmonth("March")
        # self.reg_page.set_day_ofyear("2001")
        self.reg_page.scroll_down()
        self.email = random_string.random_string_generator()+ "@gmail.com"
        self.reg_page.set_email(self.email)
        self.logger.info("******** Enter Email ********")
        self.reg_page.set_password("Manoj123")
        self.reg_page.set_confirm_password("Manoj123")
        self.logger.info("******** Enter Password And Confirm Password ********")
        self.reg_page.click_register()
        self.logger.info("******** Click Register Button ********")
        self.confirm_message = self.reg_page.get_confirm_message()
        self.logger.info("******** Check Confirmation Message ********")

        if self.confirm_message == "Your registration completed":
            assert "Test case pass: \U0001f601"
            self.driver.close()
            self.logger.info("******** Confirmation Message Checked ********")
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"account_regis.png")
            assert "Test case fail: \U0001F62C"

        self.logger.info("******** Test 001 Account Registration Ended ********")
