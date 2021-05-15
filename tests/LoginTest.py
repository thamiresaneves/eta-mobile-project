import unittest
from appium import webdriver
import time


class LoginTest(unittest.TestCase):
    def setUp(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3",
            "app": "Users/thamiresneves/Downloads/hacker_news.apk",
            "ensureWebviewsHavePages": True
        }

        self.instance = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        time.sleep(5)

    def tearDown(self):
        self.instance.quit()

    def test_login_with_empty_username_and_password(self):
        hamburger_btn = self.instance.find_element_by_accessibility_id("Navigate up")
        hamburger_btn.click()
        time.sleep(3)

        login_arrow = self.instance.find_element_by_id('com.leavjenn.hews:id/iv_expander')
        login_arrow.click()
        time.sleep(3)

        login_btn = self.instance.find_element_by_id('com.leavjenn.hews:id/design_menu_item_text')
        login_btn.click()
        time.sleep(3)

        submit_login_button = self.instance.find_element_by_id('android:id/button1')
        submit_login_button.click()
        time.sleep(3)

        error_message = self.instance.find_element_by_id('com.leavjenn.hews:id/tv_prompt').text
        expected_message = 'Catch you, anonymous!'
        self.assertEqual(expected_message, error_message)

    def test_login_with_empty_username(self):
        hamburger_btn = self.instance.find_element_by_accessibility_id("Navigate up")
        hamburger_btn.click()
        time.sleep(3)

        login_arrow = self.instance.find_element_by_id('com.leavjenn.hews:id/iv_expander')
        login_arrow.click()
        time.sleep(3)

        login_btn = self.instance.find_element_by_id('com.leavjenn.hews:id/design_menu_item_text')
        login_btn.click()
        time.sleep(3)

        password_field = self.instance.find_element_by_id('com.leavjenn.hews:id/et_password')
        password_field.send_keys('123456')

        submit_login_button = self.instance.find_element_by_id('android:id/button1')
        submit_login_button.click()
        time.sleep(3)

        error_message = self.instance.find_element_by_id('com.leavjenn.hews:id/tv_prompt').text
        expected_message = 'Catch you, anonymous!'
        self.assertEqual(expected_message, error_message)

    def test_login_with_empty_password(self):
        hamburger_btn = self.instance.find_element_by_accessibility_id("Navigate up")
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

        submit_login_button = self.instance.find_element_by_id('android:id/button1')
        submit_login_button.click()
        time.sleep(3)

        error_message = self.instance.find_element_by_id('com.leavjenn.hews:id/tv_prompt').text
        expected_message = 'You got a short…password'
        self.assertEqual(expected_message, error_message)

    def test_cancel_login(self):
        hamburger_btn = self.instance.find_element_by_accessibility_id('Navigate up')
        hamburger_btn.click()
        time.sleep(3)

        login_arrow = self.instance.find_element_by_id('com.leavjenn.hews:id/iv_expander')
        login_arrow.click()
        time.sleep(3)

        login_btn = self.instance.find_element_by_id('com.leavjenn.hews:id/design_menu_item_text')
        login_btn.click()
        time.sleep(3)

        cancel_login_button = self.instance.find_element_by_id('android:id/button2')
        cancel_login_button.click()
        time.sleep(1)

        search_btn = self.instance.find_element_by_id('com.leavjenn.hews:id/action_search')
        self.assertTrue(search_btn.is_displayed())
