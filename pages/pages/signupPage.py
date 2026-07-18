from pages.pages.Basepage import BasePage


class SignUpPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def get_url(self):
        return self.driver.current_url




