from appium.webdriver.common.mobileby import MobileBy


class LoginLocators(object):
    USERNAME_FIELD = (MobileBy.ID, 'com.leavjenn.hews:id/et_user_name')
    PASSWORD_FIELD = (MobileBy.ID, 'com.leavjenn.hews:id/et_password')
    SUBMIT_BUTTON = (MobileBy.ID, 'android:id/button1')
    CANCEL_BUTTON = (MobileBy.ID, 'android:id/button2')
    FEEDBACK_MESSAGE = (MobileBy.ID, 'com.leavjenn.hews:id/tv_prompt')
