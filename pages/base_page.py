from selenium.webdriver.common.by import By
from utils.wait import Wait
from drivers.driver_service import DriverService

class BasePage:
    def __init__(self):
        self.driver = DriverService().get_driver()
        self.wait = Wait()

    def text(self, text):
        return By.XPATH, f"//*[@text='{text}']"

    def description(self, text):
        return By.XPATH, f"//*[@content-desc='{text}']"

    def close_session(self):
        self.driver.quit()

    def install_and_open_app(self, folder_app):
        self.remove_app()
        self.install_app(folder_app)
        self.open_app()

    def remove_app(self):
        self.driver.remove_app("vivino.web.app")

    def install_app(self, folder_app):
        self.driver.install_app(folder_app)
        self.driver.implicitly_wait(2)

    def open_app(self):
        self.driver.activate_app("vivino.web.app")
