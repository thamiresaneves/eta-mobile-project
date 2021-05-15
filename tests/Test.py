import unittest
from tests.AppStart import AppStart
from pages.MainPage import MainPage
from pages.LoginPage import LoginPage
from helpers.Constants import Constants


class Test(unittest.TestCase):

    def setUp(self):
        AppStart.start(self)

    def test_login_with_empty_credentials(self):
        MainPage.access_login_pop_up()
        LoginPage.click_submit_btn()

        expected_message = Constants.ANONYMOUS_MESSAGE
        self.assertEqual(expected_message, LoginPage.get_error())

    def tearDown(self):
        AppStart.tear_down()
