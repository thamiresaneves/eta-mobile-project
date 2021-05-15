from appium.webdriver.extensions.android.gsm import GsmCallActions

from helpers.Constants import Constants
from pages.BasePage import BasePage
import time


class ManageInterruptionsPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def toggle_wifi(self):
        self.driver.toggle_wifi()

    def call_device(self):
        self.driver.make_gsm_call(Constants.PHONE_NUMBER, GsmCallActions.CALL)

    def accept_call(self):
        time.sleep(1)
        self.driver.make_gsm_call(Constants.PHONE_NUMBER, GsmCallActions.ACCEPT)

    def end_call(self):
        time.sleep(1)
        self.driver.make_gsm_call(Constants.PHONE_NUMBER, GsmCallActions.CANCEL)
