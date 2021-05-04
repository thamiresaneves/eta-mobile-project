import unittest
from appium import webdriver
import time


class LoginTest(unittest.TestCase):
    def setUp(self):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'Appium',
            'app': '/Users/thamiresneves/Downloads/hacker_news.apk'
        }

        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        time.sleep(10)

        def tearDown(self):
            self.instance.quit()

        def login_successfully(self):
            hamburger_btn = self.instance.find_element_by_accessibility_id('Navigate up')
            login_arrow = self.instance.find_element_by_accessibility_id('com.leavjenn.hews:id/iv_expander')
            login_btn = self.instance.find_element_by_accessibility_id('com.leavjenn.hews:id/design_menu_item_text')
            username_field = self.instance.find_element_by_accessibility_id('com.leavjenn.hews:id/et_user_name')
            password_field = self.instance.find_element_by_accessibility_id(' com.leavjenn.hews:id/et_password')
            submit_login_button = self.instance.find_element_by_accessibility_id('ndroid:id/button1')
            error_message = self.instance.find_element_by_accessibility_id('com.leavjenn.hews:id/tv_prompt')
            login_title = self.instance.find_element_by_accessibility_id('android:id/alertTitle')
            cancel_login_button = self.instance.find_element_by_accessibility_id('cancelBtn = android:id/button2')

            anonymous_message = 'Catch you, anonymous!'
            invalid_password_message = 'You got a short…password'

        def login_with_no_username(self):
            pass

        def login_with_no_password(self):
            pass

        def cancel_login(self):
            pass
