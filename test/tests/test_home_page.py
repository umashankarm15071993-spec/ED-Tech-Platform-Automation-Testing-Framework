from pages.pages.homepage import HomePage
import config
from pages.pages.signupPage import SignUpPage
from utilities.utilities.logger import LogGen


class TestHomePage:


    logger=LogGen.loggen()

    def test_Tc01_test_open_url(self,driver):
        self.logger.info("**** TC01- Verify Application Url Started ****")
        self.logger.info("**** Application  Started ****")
        homepage=HomePage(driver)
        self.logger.info("**** Validate The URL ****")
        assert homepage.get_url() == config.BASE_URL
        self.logger.info("**** TC-01-Passed ****")


    def test_Tc02_test_verify_title(self,driver):
        self.logger.info("**** TC02- Verify Title ****")
        self.logger.info("**** Application  Started ****")
        homepage=HomePage(driver)
        self.logger.info("**** Validate The Title of the Page ****")
        assert homepage.get_title() == config.EXPECTED_TITLE
        self.logger.info("**** TC-02-Passed ****")


    def test_Tc03_test_verify_login_button_(self,driver):
        self.logger.info("**** TC03- Verify Login Button  ****")
        self.logger.info("**** Application  Started ****")
        homepage=HomePage(driver)
        self.logger.info("**** Validate The Home Page Login Button Visible ****")
        assert homepage.is_displayed(homepage.LOGIN_BUTTON)
        homepage.click_login()
        self.logger.info("**** Validate The Home Page Login Button Clickable ****")
        assert homepage.get_url() in config.LOGIN_PAGE_URL
        self.logger.info("**** TC-03-Passed ****")


    def test_Tc04_test_verify_signin_button(self,driver):
        self.logger.info("**** TC04- verify Signin Button ****")
        self.logger.info("**** Application  Started ****")
        homepage=HomePage(driver)
        signup=SignUpPage(driver)
        self.logger.info("**** Validate The Home Page Signin Button Visible  ****")
        assert homepage.is_displayed(HomePage.SIGN_UP_BUTTON)
        homepage.click_signup()
        self.logger.info("**** Validate The Home Page Sign Button Clickable ****")
        assert signup.get_url() in config.SIGNUP_PAGE_URL
        self.logger.info("**** TC-04-Passed ****")


    def test_Tc08_verify_menu_bar(self,driver):
        self.logger.info("**** TC08- verify Menu Bar ****")
        self.logger.info("**** Application  Started ****")
        homepage=HomePage(driver)
        self.logger.info("**** Validate The Menu Bar ****")
        assert homepage.verify_menu()
        self.logger.info("**** TC-08-Passed ****")

    def test_Tc09_validate_chatbot(self,driver):
        self.logger.info("**** TC09- verify ChatBot ****")
        self.logger.info("**** Application  Started ****")
        homepage=HomePage(driver)
        self.logger.info("**** Validate The Chat Board ****")
        assert homepage.verify_dobby()
        self.logger.info("**** TC-09-Passed ****")





