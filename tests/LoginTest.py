import time

from tests.BaseTest import BaseTest
from helpers.Constants import Constants


class Test(BaseTest):

    def test_login_with_empty_credentials(self):
        self.app.mainPage.access_login_pop_up()
        self.app.loginPage.click_submit_btn()

        expected_message = Constants.ANONYMOUS_MESSAGE
        self.assertEqual(expected_message, self.app.loginPage.get_error())

    def test_login_with_empty_username(self):
        self.app.mainPage.access_login_pop_up()
        self.app.loginPage.fill_password(Constants.INVALID_PASSWORD)
        self.app.loginPage.click_submit_btn()

        expected_message = Constants.ANONYMOUS_MESSAGE
        self.assertEqual(expected_message, self.app.loginPage.get_error())

    def test_login_with_empty_password(self):
        self.app.mainPage.access_login_pop_up()
        self.app.loginPage.fill_username(Constants.INVALID_USERNAME)
        self.app.loginPage.click_submit_btn()

        expected_message = Constants.SHORT_PASSWORD_MESSAGE
        self.assertEqual(expected_message, self.app.loginPage.get_error())

    def test_login_with_invalid_credentials(self):
        self.app.mainPage.access_login_pop_up()
        self.app.loginPage.fill_username(Constants.INVALID_USERNAME)
        self.app.loginPage.fill_password(Constants.INVALID_PASSWORD)
        self.app.loginPage.click_submit_btn()

        expected_message = Constants.WRONG_USERNAME_PASSWORD_MESSAGE
        self.assertEqual(expected_message, self.app.loginPage.get_error())

    def test_cancel_login(self):
        self.app.mainPage.access_login_pop_up()
        self.app.loginPage.click_cancel_btn()

        search_button = self.app.mainPage.get_search_button()
        self.assertTrue(search_button.is_displayed())

    def test_login_with_valid_credentials(self):
        self.app.mainPage.access_login_pop_up()
        self.app.loginPage.login(Constants.VALID_USERNAME, Constants.VALID_PASSWORD)

        time.sleep(3)
        self.app.mainPage.click_hamburger_menu()

        logged_user = Constants.VALID_USERNAME
        self.assertEqual(logged_user, self.app.mainPage.get_logged_user())

