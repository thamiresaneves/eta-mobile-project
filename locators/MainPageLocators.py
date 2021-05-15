from appium.webdriver.common.mobileby import MobileBy


class MainPageLocators(object):
    # Top bar locators
    SEARCH_BTN = (MobileBy.ID, 'com.leavjenn.hews:id/action_search')
    HAMBURGER_BTN = (MobileBy.ACCESSIBILITY_ID, 'Navigate up')

    # Menu locators
    ARROW_BTN = (MobileBy.ID, 'com.leavjenn.hews:id/iv_expander')
    LOGIN_BTN = (MobileBy.ID, 'com.leavjenn.hews:id/design_menu_item_text')
