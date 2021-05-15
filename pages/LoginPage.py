import time

from locators.LoginLocators import LoginLocators
from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

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
        time.sleep(2)
        return BasePage.find_element(self.driver, LoginLocators.FEEDBACK_MESSAGE).text

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_submit_btn()

    def get_username(self):
        return BasePage.find_element(self.driver, LoginLocators.USERNAME_FIELD).text

    def get_password(self):
        return BasePage.find_element(self.driver, LoginLocators.PASSWORD_FIELD).text
