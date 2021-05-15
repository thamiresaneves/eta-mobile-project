import unittest
from appium import webdriver
import time

from appium.webdriver.extensions.android.gsm import GsmCallActions


class ManageInterruptions(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3",
            "app": "Users/thamiresneves/Downloads/hacker_news.apk",
            "ensureWebviewsHavePages": True,
        }

        self.instance = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        time.sleep(5)

    def tearDown(self):
        self.instance.quit()

    def test_login_without_network(self):
        self.instance.toggle_wifi()
        hamburger_btn = self.instance.find_element_by_accessibility_id('Navigate up')
        hamburger_btn.click()
        time.sleep(3)

        login_arrow = self.instance.find_element_by_id('com.leavjenn.hews:id/iv_expander')
        login_arrow.click()
        time.sleep(3)

        login_btn = self.instance.find_element_by_id('com.leavjenn.hews:id/design_menu_item_text')
        login_btn.click()
        time.sleep(3)

        username_field = self.instance.find_element_by_id('com.leavjenn.hews:id/et_user_name')
        username_field.send_keys('Joao')

        password_field = self.instance.find_element_by_id('com.leavjenn.hews:id/et_password')
        password_field.send_keys('123456')

        submit_login_button = self.instance.find_element_by_id('android:id/button1')
        submit_login_button.click()
        time.sleep(3)

        error_message = self.instance.find_element_by_id('com.leavjenn.hews:id/tv_prompt').text
        expected_message = 'Arrr…wrong username/password'
        self.assertEqual(expected_message, error_message)

        self.instance.toggle_wifi()

    def test_simulate_call(self):
        hamburger_btn = self.instance.find_element_by_accessibility_id('Navigate up')
        hamburger_btn.click()
        time.sleep(3)

        login_arrow = self.instance.find_element_by_id('com.leavjenn.hews:id/iv_expander')
        login_arrow.click()
        time.sleep(3)

        login_btn = self.instance.find_element_by_id('com.leavjenn.hews:id/design_menu_item_text')
        login_btn.click()
        time.sleep(3)

        username_field = self.instance.find_element_by_id('com.leavjenn.hews:id/et_user_name')
        username_field.send_keys('Joao')

        password_field = self.instance.find_element_by_id('com.leavjenn.hews:id/et_password')
        password_field.send_keys('123456')

        self.instance.make_gsm_call('5551234567', GsmCallActions.CALL)
        time.sleep(2)
        self.instance.make_gsm_call("5551234567", GsmCallActions.ACCEPT)
        time.sleep(1)
        self.instance.make_gsm_call("5551234567", GsmCallActions.CANCEL)

        username = username_field.text
        password = password_field.text
        self.assertEqual(username, 'Joao')
        self.assertEqual(password, '••••••')


