from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from drivers.driver_service import DriverService

class Wait:
    def __init__(self, duration=30):
        self.duration = duration

    def set_wait(self, duration):
        self.duration = duration
        return self

    def visibility(self, by: By):
        wait = WebDriverWait(DriverService().get_driver(), self.duration)
        return wait.until(EC.visibility_of_element_located(by))

    def clickable(self, by: By):
        wait = WebDriverWait(DriverService().get_driver(), self.duration)
        return wait.until(EC.element_to_be_clickable(by))
