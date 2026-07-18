from selenium.webdriver.common.by import By
from pages.pages.Basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    LOGIN_BUTTON=(By.ID,"login-btn")
    SIGN_UP_BUTTON=(By.XPATH,"//button[contains(text(),'Sign up')]")
    LIVE_CLASSES=(By.XPATH,"//div[@id='solutions']/p[contains(text(),'LIVE Classes')]")
    COURSES=(By.XPATH,"//div[@id='solutions']/p[contains(text(),'Courses')]")
    PRACTICE=(By.XPATH,"//div[@id='solutions']/p[contains(text(),'Practice')]")
    RESOURCE=(By.XPATH,"//div[@id='solutions']/p[contains(text(),'Resources')]")
    OUR_PRODUCTS=(By.XPATH,"//div[@id='solutions']/p[contains(text(),'Our Products')]")
    containers=[LIVE_CLASSES,COURSES,PRACTICE,RESOURCE,OUR_PRODUCTS]
    CHAT_BOT=(By.ID,'zs_fl_chat')


    def __init__(self,driver):
        super().__init__(driver)


    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def click_signup(self):
        self.click(self.SIGN_UP_BUTTON)

    def verify_menu(self):
        for container in self.containers:
            if not self.driver.find_element(*container).is_displayed():
                return False

        return True

    def verify_dobby(self):
        chatbot=self.get_locator(self.CHAT_BOT)
        return chatbot.is_displayed()









