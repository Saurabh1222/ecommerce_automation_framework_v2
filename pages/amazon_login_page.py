from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class AmazonLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.amazon.com")

    # Locators for Amazon's sign-in flow
    ACCOUNT_AND_LISTS_NAV = (By.ID, "nav-link-accountList")
    SIGN_IN_BUTTON_ON_MENU = (By.CSS_SELECTOR, "#nav-flyout-accountList .nav-action-button")
    EMAIL_INPUT = (By.ID, "ap_email")
    CONTINUE_BUTTON = (By.ID, "continue")
    PASSWORD_INPUT = (By.ID, "ap_password")
    LOGIN_BUTTON = (By.ID, "signInSubmit")

    # Methods to interact with the page
    def navigate_to_login(self):
        account_nav = self.find_element(self.ACCOUNT_AND_LISTS_NAV)
        ActionChains(self.driver).move_to_element(account_nav).perform()
        sign_in_button = self.find_element(self.SIGN_IN_BUTTON_ON_MENU)
        sign_in_button.click()

    def enter_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)