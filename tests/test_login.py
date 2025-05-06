import allure
import pytest

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_log_in_email(self):
        allure.dynamic.title("Checking login")
        login_page = self.login_page
        login_page.click_email_enter_btn()
        assert login_page.check_text("What’s your email?").is_displayed()

        login_page.enter_email().click_next_button()
        assert login_page.check_text("Welcome back! Log in to your Vivino account").is_displayed()

        login_page.enter_password().click_log_in_btn()
        home_page = login_page.get_main_page()
        assert home_page.check_text("Find friends").is_displayed()
        assert home_page.check_text("Top-rated wines").is_displayed()

    @pytest.fixture(scope="class", autouse=True)
    def teardown(self):
        yield
        self.login_page.close_session()
