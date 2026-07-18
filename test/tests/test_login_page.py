from pages.pages.LoginPage import LoginPage
from pages.pages.homepage import HomePage
import config
from utilities.utilities.excelutilites import ExcelUtilities
from utilities.utilities.logger import LogGen

file = "E:/Guvi_projects/testdata/testadata.xlsx"
sheet="Sheet1"


class TestLoginPage:

    logger=LogGen.loggen()


    def test_Tc06_test_valid_login(self,driver):
        self.logger.info("******** TC06 - verify valid login *******")
        self.logger.info("**** Application Lunch the Url ****")
        login=LoginPage(driver)
        homepage=HomePage(driver)
        self.logger.info("**** Click the Homepage Login Button ****")
        homepage.click_login()
        self.logger.info("**** Enter The Valid Email ****")
        login.enter_email(config.VALID_EMAIL)
        self.logger.info("**** Enter The Valid Password ****")
        login.enter_password(config.VALID_PASSWORD)
        self.logger.info("**** Click Login Button ****")
        login.click_login()
        self.logger.info("**** Validate the expected URL ****")
        assert config.DASHBOARD_URL in login.get_url()
        self.logger.info("**** TC-06-Passed ****")

    def test_Tc07_test_invalid_login(self,driver):
        self.logger.info("******** TC07 - Verify Invalid Login Started ********")
        login=LoginPage(driver)
        row=ExcelUtilities.get_row(file,sheet)
        self.logger.info("**** Click the Homepage Login Button ****")
        login.click_login()

        for row in range(2,row+1):

            self.logger.info(f"Executing Test Data Row : {row}")
            username=ExcelUtilities.read_data(file,sheet,row,1)
            password=ExcelUtilities.read_data(file,sheet,row,2)
            self.logger.info(f"Entering Username : {username}")
            self.logger.info(f"Entering Password : {password}")

            login.enter_email(username)
            login.enter_password(password)
            self.logger.info("Clicking Login Button")
            login.click_login()

            actual_title=login.get_title()
            expected_title="HCL GUVI | Login"

            self.logger.info("**** Validate Title ****")
            assert actual_title ==  expected_title
            self.logger.info("******** TC07 Passed ********")

    def test_Tc10_verify_logout(self,driver):
        self.logger.info("******** TC10 - Verify Logout Successful *******")
        home=HomePage(driver)
        login=LoginPage(driver)
        home.click_login()
        self.logger.info("**** Enter The Valid Email ****")
        login.enter_email(config.VALID_EMAIL)
        self.logger.info("**** Enter The Valid Password ****")
        login.enter_password(config.VALID_PASSWORD)
        self.logger.info("**** Click Login Button ****")
        login.click_login()
        self.logger.info("**** Verify Logout Successful ****")
        login.click_logout()
        self.logger.info("**** Verify Logout Redirected expected URL ****")
        assert login.get_url() == config.DASHBOARD_URL
        self.logger.info("**** TC-10-Passed ****")














