from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        try:
            wait = WebDriverWait(self, 5)
            return wait.until(EC.presence_of_element_located(self.driver.find_element(*locator)))
        except:
            return 'Element not found'
