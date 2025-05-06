from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class WineDetailsPage(BasePage):
    STARS_RATING = (By.ID, "vivino.web.app:id/star_rating")
    RATING_COUNT = (By.ID, "vivino.web.app:id/rating_count")
    AVG_PRICE_VALUE = (By.ID, "vivino.web.app:id/avg_price_value")
    AVG_PRICE_LABEL = (By.ID, "vivino.web.app:id/avg_price_label")

    @allure.step("Check text on the page")
    def check_text(self, text):
        return self.wait.visibility(self.text(text))
