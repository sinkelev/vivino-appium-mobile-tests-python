import json
import os

import pytest
from drivers.capability import Capability
from drivers.initial_driver import set_driver
from pages.login_page import LoginPage


with open(os.path.join(os.path.dirname(__file__), 'config', 'devices.json')) as f:
    devices = json.load(f)["devices"]

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://localhost:4723", help="Appium server URL")

@pytest.fixture(scope="function", params=devices)
def setup(request):
    device = request.param
    url = request.config.getoption("--url")
    platform_name = device["platformName"]
    automation_name = device["automationName"]
    device_name = device["deviceName"]
    udid = device["udid"]
    platform_version = device["platformVersion"]
    app_activity = device["appActivity"]

    capability = Capability(url, platform_name, automation_name, device_name, udid, platform_version, app_activity)
    set_driver(capability)

    apk_path = os.path.join(os.path.dirname(__file__), 'apk', 'vivino.apk')

    if not os.path.exists(apk_path):
        raise FileNotFoundError(f"APK file not found at path: {apk_path}")

    login_page = LoginPage()
    login_page.install_and_open_app(apk_path)
    request.cls.login_page = login_page
