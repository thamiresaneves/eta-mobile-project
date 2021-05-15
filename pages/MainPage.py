from pages.BasePage import BasePage
from locators.MainPageLocators import MainPageLocators


class MainPage(BasePage):

    def access_login_pop_up(self):
        hamburger_menu = BasePage.find_element(self.driver, MainPageLocators.HAMBURGER_BTN)
        hamburger_menu.click()

        arrow_btn = BasePage.find_element(self.driver, MainPageLocators.ARROW_BTN)
        arrow_btn.click()

        login_btn = BasePage.find_element(self.driver, MainPageLocators.LOGIN_BTN)
        login_btn.click()