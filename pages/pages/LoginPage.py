from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from pages.pages.Basepage import BasePage


class LoginPage(BasePage):


    EMAIL_TEXT_BOX=(By.ID,"email")
    PASSWORD_TEXT_BOX=(By.ID,"password")
    LOGIN_BUTTON=(By.ID,"login-btn")
    EMAIL_ERROR=(By.XPATH, "//div[@id='emailgroup']//div[contains(@class,'invalid-feedback')]")
    PASSWORD_ERROR=(By.XPATH,"//div[@id='passwordgroup']//div[contains(@class,'invalid-feedback')]")
    EMPTY_EMAIL_ERROR_MESSAGE = " Hmm...that doesnt look like an email address. Try again."
    EMPTY_PASSWORD_ERROR_MESSAGE = " Password should not be empty."
    INCORRECT_ERROR_MESSAGE = "Incorrect Email or Password"
    LOGOUT_IMG=(By.XPATH,"//img[@alt='Profile']")
    SIGN_OUT=(By.XPATH,"//p[contains(text(),'Sign Out')]")

    def __init__(self,driver):
        super().__init__(driver)

    def enter_email(self,email):
        self.enter_text(self.EMAIL_TEXT_BOX,email)

    def enter_password(self,pass_word):
        self.enter_text(self.PASSWORD_TEXT_BOX,pass_word)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def click_logout(self):
        try:
            self.click(self.LOGOUT_IMG)
            self.click(self.SIGN_OUT)
        except TimeoutException:
            return False








