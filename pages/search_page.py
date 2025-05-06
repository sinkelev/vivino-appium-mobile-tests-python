from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.wine_details_page import WineDetailsPage
import allure

class SearchPage(BasePage):
    SEARCH_INPUT = (By.XPATH, "//android.widget.EditText[@text='Search for wine']")
    ALL_WINES_BTN = (By.XPATH, "//android.widget.TextView[@text='All Wines']")
    MY_WINES_BTN = (By.XPATH, "//android.widget.TextView[@text='My Wines']")
    PEOPLE_BTN = (By.XPATH, "//android.widget.TextView[@text='People']")

    @allure.step("Enter wine")
    def enter_wine(self, wine):
        search_input = self.wait.visibility(self.SEARCH_INPUT)
        search_input.click()
        search_input.send_keys(wine)
        return self

    @allure.step("Click on text")
    def click_text(self, text):
        element = self.wait.clickable((By.XPATH, f"//*[contains(@text,'{text}')]"))
        element.click()
        return self

    @allure.step("Open Wine Details Page")
    def get_wine_details_page(self):
        return WineDetailsPage()

    @allure.step("Check text on the page")
    def check_text(self, text):
        return self.wait.visibility(self.text(text))
