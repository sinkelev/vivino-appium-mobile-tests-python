from appium import webdriver
from drivers.capability import Capability
from utils.singleton import Singleton

class DriverService(metaclass=Singleton):
    def __init__(self):
        self.driver = None

    def set_driver(self, capability: Capability):
        self.driver = webdriver.Remote(capability.url, options=capability.get_property())

    def get_driver(self):
        return self.driver