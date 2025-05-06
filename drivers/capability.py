from appium.options.android import UiAutomator2Options
from dataclasses import dataclass

@dataclass
class Capability:
    url: str
    platform_name: str
    automation_name: str
    device_name: str
    udid: str
    platform_version: str
    app_activity: str

    def get_property(self):
        options = UiAutomator2Options()
        options.set_capability("enforceXPath1", True)
        options.set_capability("allowInvisibleElements", True)
        options.set_capability("ignoreUnimportantViews", False)
        options.set_capability("autoAcceptAlerts", True)
        options.set_capability("unicodeKeyboard", True)
        options.set_capability("resetKeyboard", True)
        options.set_capability("maxInstances", 1)
        options.set_capability("platformName", self.platform_name)
        options.set_capability("automationName", self.automation_name)
        options.set_capability("adbExecTimeout", 600000)
        options.set_capability("androidInstallTimeout", 600000)
        options.set_capability("deviceName", self.device_name)
        options.set_capability("udid", self.udid)
        options.set_capability("platformVersion", self.platform_version)
        options.set_capability("enforceAppInstall", True)
        options.auto_grant_permissions = True
        options.set_capability("appActivity", self.app_activity)
        options.set_capability("newCommandTimeout", 120)
        return options