from selenium.webdriver.common.by import By


class LoginPage():
    email_xpath = '//*[@id="Email"]'
    password_xpath = '//*[@id="Password"]'
    login_button_xpath = '//*[@class="button-1 login-button"]'
    logout_xpath = '//*[@class="ico-logout"]'

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self,login_email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(login_email)

    def enter_password(self,login_password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(login_password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def get_logout_text(self):
        try:
            return self.driver.find_element(By.XPATH, self.logout_xpath).text
        except:
            None