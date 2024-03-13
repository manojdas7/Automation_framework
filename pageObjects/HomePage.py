from selenium.webdriver.common.by import By

class Homepage():
    login_class = 'ico-login'
    register_xpath = "//a[@class='ico-register']"

    def __init__(self,driver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element(By.CLASS_NAME,value= self.login_class).click()

    def click_register(self):
        self.driver.find_element(By.XPATH,value= self.register_xpath).click()