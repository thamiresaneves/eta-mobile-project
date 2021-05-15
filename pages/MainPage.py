import time

from locators.MainPageLocators import MainPageLocators
from pages.BasePage import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def click_hamburger_menu(self):
        time.sleep(1)
        hamburger_menu = BasePage.find_element(self.driver, MainPageLocators.HAMBURGER_BTN)
        hamburger_menu.click()

    def access_login_pop_up(self):
        self.click_hamburger_menu()
        arrow_btn = BasePage.find_element(self.driver, MainPageLocators.ARROW_BTN)
        arrow_btn.click()
        logout_btn = BasePage.find_element(self.driver, MainPageLocators.LOGIN_BTN)
        logout_btn.click()

    def get_search_button(self):
        return BasePage.find_element(self.driver, MainPageLocators.SEARCH_BTN)

    def get_logged_user(self):
        return BasePage.find_element(self.driver, MainPageLocators.LOGGED_USER_ACCOUNT).text
