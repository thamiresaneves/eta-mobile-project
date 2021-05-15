from appium import webdriver
from pages import MainPage


class AppStart:

    def start(self):
        caps = {
            'platformName': 'Android',
            'deviceName': 'Pixel 3',
            'app': 'Users/thamiresneves/Downloads/hacker_news.apk',
            'ensureWebviewsHavePages': True
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return MainPage

    def tear_down(self):
        self.driver.quit()
