from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
import allure

class LoginPage(BasePage):
    EMAIL_ENTER_BTN = (By.ID, "vivino.web.app:id/btn_email_continue")
    EMAIL_INPUT = (By.ID, "vivino.web.app:id/edit_text")
    NEXT_BTN = (By.ID, "vivino.web.app:id/btn_fb_continue")
    PASSWORD_INPUT = (By.XPATH, "//*[@text='Password']")
    LOG_IN_BTN = (By.XPATH, "//android.widget.Button[@text='Log in']")

    @allure.step("Click on 'Continue with email'")
    def click_email_enter_btn(self):
        self.driver.find_element(*self.EMAIL_ENTER_BTN).click()
        return self

    @allure.step("Enter email")
    def enter_email(self):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys("apple_909@mail.ru")
        return self

    @allure.step("Click 'Continue'")
    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BTN).click()
        return self

    @allure.step("Enter password")
    def enter_password(self):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys("111111Qw")
        return self

    @allure.step("Click on 'Log in'")
    def click_log_in_btn(self):
        self.driver.find_element(*self.LOG_IN_BTN).click()
        return self

    @allure.step("Open Home page")
    def get_main_page(self):
        return HomePage()

    @allure.step("Check text on the page")
    def check_text(self, text):
        return self.wait.visibility(self.text(text))