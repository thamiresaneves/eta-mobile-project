import unittest

from appium import webdriver
from helpers.Application import Application


class BaseTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Pixel 3',
            'app': 'Users/thamiresneves/Downloads/hacker_news.apk',
            'ensureWebviewsHavePages': True
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.app = Application(self.driver)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
