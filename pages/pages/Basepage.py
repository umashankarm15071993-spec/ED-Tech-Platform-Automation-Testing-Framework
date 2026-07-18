from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
from utilities.utilities.logger import LogGen


class BasePage:

    logger=LogGen.loggen()

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver, config.EXPLICIT_WAIT)

    def click(self,locator):
        try:
            element=self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            self.logger.error(f"Error While Clicking:{e}")
            raise


    def enter_text(self,locator,text):
        element=self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys("" if text is None else text)

    def is_displayed(self,locator):
        try:
            element=self.wait.until(EC.presence_of_element_located(locator))
            return element.is_displayed()
        except TimeoutException:
            return False

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.get_attribute("innerText").strip()

    def get_locator(self,locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

