from pages.BasePage import BasePage
from locators.LoginLocators import LoginLocators


class LoginPage(BasePage):

    def fill_username(self, username):
        username_field = BasePage.find_element(self.driver, LoginLocators.USERNAME_FIELD)
        username_field.send_keys(username)

    def fill_password(self, password):
        password_field = BasePage.find_element(self.driver, LoginLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

    def click_submit_btn(self):
        submit_btn = BasePage.find_element(self.driver, LoginLocators.SUBMIT_BUTTON)
        submit_btn.click()

    def click_cancel_btn(self):
        cancel_btn = BasePage.find_element(self.driver, LoginLocators.CANCEL_BUTTON)
        cancel_btn.click()

    def get_error(self):
        return BasePage.find_element(self.driver, LoginLocators.FEEDBACK_MESSAGE).text
