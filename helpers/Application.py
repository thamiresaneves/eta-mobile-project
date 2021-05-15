from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.ManageInterruptionsPage import ManageInterruptionsPage


class Application:
    def __init__(self, driver):
        self.mainPage = MainPage(driver)
        self.loginPage = LoginPage(driver)
        self.manageInterruptions = ManageInterruptionsPage(driver)
