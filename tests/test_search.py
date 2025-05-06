import pytest
import allure

@pytest.mark.usefixtures("setup")
class TestSearch:
    def test_search_open(self):
        allure.dynamic.title("Checking the opening of the search page")
        login_page = self.login_page
        login_page.click_email_enter_btn()
        assert login_page.check_text("What’s your email?").is_displayed()

        login_page.enter_email().click_next_button()
        assert login_page.check_text("Welcome back! Log in to your Vivino account").is_displayed()

        login_page.enter_password().click_log_in_btn()
        home_page = login_page.get_main_page()
        assert home_page.check_text("Find friends").is_displayed()
        assert home_page.check_text("Top-rated wines").is_displayed()

        home_page.click_search_input()
        search_page = home_page.get_search_page()
        assert search_page.check_text("Search for wine").is_displayed()
        assert search_page.check_text("All Wines").is_displayed()
        assert search_page.check_text("My Wines").is_displayed()
        assert search_page.check_text("People").is_displayed()

    def test_search_wine(self):
        allure.dynamic.title("Checking out search results when entering a request")
        login_page = self.login_page
        login_page.click_email_enter_btn()
        assert login_page.check_text("What’s your email?").is_displayed()

        login_page.enter_email().click_next_button()
        assert login_page.check_text("Welcome back! Log in to your Vivino account").is_displayed()

        login_page.enter_password().click_log_in_btn()
        home_page = login_page.get_main_page()
        assert home_page.check_text("Find friends").is_displayed()
        assert home_page.check_text("Top-rated wines").is_displayed()

        home_page.click_search_input()
        search_page = home_page.get_search_page()
        assert search_page.check_text("Search for wine").is_displayed()
        assert search_page.check_text("All Wines").is_displayed()
        assert search_page.check_text("My Wines").is_displayed()
        assert search_page.check_text("People").is_displayed()

        search_page.enter_wine("Matsu")
        assert home_page.check_text("Matsu").is_displayed()
        assert home_page.check_text("El Picaro").is_displayed()

    def test_search_wine_detail(self):
        allure.dynamic.title("Checking the transition to the detailed page of wine from the search page")
        login_page = self.login_page
        login_page.click_email_enter_btn()
        assert login_page.check_text("What’s your email?").is_displayed()

        login_page.enter_email().click_next_button()
        assert login_page.check_text("Welcome back! Log in to your Vivino account").is_displayed()

        login_page.enter_password().click_log_in_btn()
        home_page = login_page.get_main_page()
        assert home_page.check_text("Find friends").is_displayed()
        assert home_page.check_text("Top-rated wines").is_displayed()

        home_page.click_search_input()
        search_page = home_page.get_search_page()
        assert search_page.check_text("Search for wine").is_displayed()
        assert search_page.check_text("All Wines").is_displayed()
        assert search_page.check_text("My Wines").is_displayed()
        assert search_page.check_text("People").is_displayed()

        search_page.enter_wine("Matsu")
        assert home_page.check_text("Matsu").is_displayed()
        assert home_page.check_text("El Picaro").is_displayed()

        search_page.click_text("El Picaro")
        wine_details_page = search_page.get_wine_details_page()
        assert wine_details_page.check_text("Matsu").is_displayed()
        assert wine_details_page.check_text("El Picaro").is_displayed()
        assert wine_details_page.driver.find_element(*wine_details_page.STARS_RATING).is_displayed()
        assert wine_details_page.driver.find_element(*wine_details_page.RATING_COUNT).is_displayed()
        assert wine_details_page.driver.find_element(*wine_details_page.AVG_PRICE_VALUE).is_displayed()
        assert wine_details_page.driver.find_element(*wine_details_page.AVG_PRICE_LABEL).is_displayed()

    @pytest.fixture(scope="class", autouse=True)
    def teardown(self):
        yield
        self.login_page.close_session()
