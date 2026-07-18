from pages.pages.homepage import HomePage
import config
from utilities.utilities.logger import LogGen


class TestSignUp:

    logger=LogGen.loggen()

    def test_Tc05_test_verify_signup(self,driver):
        self.logger.info("**** TC05- Verify Signup Button ****")
        self.logger.info("**** Application Started ****")
        homepage=HomePage(driver)
        self.logger.info("**** Click Signup Button ****")
        homepage.click_signup()
        self.logger.info("**** Validate Signup Button ****")
        assert homepage.get_url() in config.SIGNUP_PAGE_URL
        self.logger.info("**** TC-05-Passed ****")


