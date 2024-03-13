from selenium.webdriver.common.by import By

class AccountRegistrationPage():
    gender_xpath = "//input[@id='gender-male']"
    first_name_id = "FirstName"
    last_name_id = "LastName"
    dayofbirth_xpath = "//select[@name='DateOfBirthDay']"
    monthofbirth_xpath = "//select[@name='DateOfBirthMonth']"
    yearofbirth_xpath = "//select[@name='DateOfBirthYear']"
    email_xpath = '//*[@id="Email"]'
    password_xpath = "//input[@id='Password']"
    confirm_password_xpath = "//input[@id='ConfirmPassword']"
    register_xpath = "//button[@id='register-button']"
    registersucessful_xpath = "//div[@class='result']"
    continue_xpath = "//a[@class='button-1 register-continue-button']"  \
                     # "//a[normalize-space()='Continue']"


    def __init__(self,driver):
        self.driver = driver
    def set_gender(self):
        self.driver.find_element(By.XPATH, value= self.gender_xpath).click()

    def set_firstname(self,f_name):
        self.driver.find_element(By.ID, self.first_name_id).send_keys(f_name)

    def set_lastname(self,l_name):
        self.driver.find_element(By.ID, self.last_name_id).send_keys(l_name)

    def set_day_ofbirth(self,day):
        self.set_day =self.driver.find_element(By.XPATH, self.dayofbirth_xpath)
        self.set_day.selectByValue(day)

    def set_day_ofmonth(self,month):
        self.driver.find_element(By.XPATH, self.monthofbirth_xpath).selectByVisibleText(month)
    def set_day_ofyear(self,year):
        self.driver.find_element(By.XPATH, self.yearofbirth_xpath).selectByvalue(year)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 860)")  # used to scroll page down
    def set_email(self,email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def set_password(self,password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def set_confirm_password(self,confirm_password):
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(confirm_password)

    def click_register(self):
        self.driver.find_element(By.XPATH, self.register_xpath).click()

    def get_confirm_message(self):
        try:
            return self.driver.find_element(By.XPATH, self.registersucessful_xpath).text
        except:
            None