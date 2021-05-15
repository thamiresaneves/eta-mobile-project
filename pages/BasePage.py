from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.drive = driver

    def find_element(self, element):
        wait = WebDriverWait(self, 5)
        mobile_element = wait.until(EC.presence_of_element_located(element))
        return mobile_element
