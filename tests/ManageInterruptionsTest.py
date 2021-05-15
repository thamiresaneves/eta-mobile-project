from helpers.Constants import Constants
from tests.BaseTest import BaseTest


class ManageInterruptions(BaseTest):

    def test_login_without_network(self):
        self.app.manageInterruptions.toggle_wifi()
        self.app.mainPage.access_login_pop_up()
        self.app.loginPage.login(Constants.VALID_CREDENTIALS, Constants.VALID_CREDENTIALS)

        error_message = self.app.loginPage.get_error()
        expected_message = Constants.NO_INTERNET_MESSAGE
        self.assertEqual(expected_message, error_message)

        self.app.manageInterruptions.toggle_wifi()

    def test_simulate_call(self):
        self.app.mainPage.access_login_pop_up()
        self.app.loginPage.fill_username(Constants.VALID_CREDENTIALS)
        self.app.loginPage.fill_password(Constants.VALID_CREDENTIALS)

        self.app.manageInterruptions.call_device()
        self.app.manageInterruptions.accept_call()
        self.app.manageInterruptions.end_call()

        username = self.app.loginPage.get_username()
        password = self.app.loginPage.get_password()
        self.assertEqual(username, Constants.VALID_CREDENTIALS)
        self.assertEqual(password, Constants.PASSWORD_ENCRYPTED)

