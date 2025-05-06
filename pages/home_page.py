from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage
import allure

class HomePage(BasePage):
    SEARCH_INPUT = (By.XPATH, "//*[@content-desc='Search']")

    @allure.step("Click search input")
    def click_search_input(self):
        self.driver.find_element(*self.SEARCH_INPUT).click()
        return self

    @allure.step("Open Search page")
    def get_search_page(self):
        return SearchPage()

    @allure.step("Check text on the page")
    def check_text(self, text):
        return self.wait.visibility(self.text(text))
