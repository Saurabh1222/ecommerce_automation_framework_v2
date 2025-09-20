from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class AmazonLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.amazon.com")
    
    # New Locator for the "Continue" button
    
    CONTINUE_BUTTON1 = (By.XPATH, "//button[@alt='Continue shopping']")
    CONTINUE_BUTTON2 = (By.ID, "continue")

    # Locators for Amazon's sign-in flow
    ACCOUNT_AND_LISTS_NAV = (By.ID, "nav-link-accountList")
    # This locator targets the Sign in button within the hover menu
    SIGN_IN_BUTTON_ON_MENU = (By.XPATH, "//span[text()='Sign in']/parent::a")
    
    EMAIL_INPUT = (By.ID, "ap_email_login")
    
    PASSWORD_INPUT = (By.ID, "ap_password")
    LOGIN_BUTTON = (By.ID, "signInSubmit")

    def click_continue1(self):
        """
        Clicks the 'Continue' button on the login page.
        """
        try:
            # Wait for the button to be clickable
            self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON1))
            # Find the button and click it
            self.click(self.CONTINUE_BUTTON1)
        except Exception as e:
            raise Exception(f"Failed to click the 'Continue' button. Error: {e}")

    # Methods to interact with the page
    def navigate_to_login(self):
        # Find the main account navigation element
        account_nav = self.find_element(self.ACCOUNT_AND_LISTS_NAV)
        
        # Hover over the element to make the dropdown menu appear
        ActionChains(self.driver).move_to_element(account_nav).perform()
        # Explicitly wait for the "Sign in" button to be clickable
        self.wait.until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON_ON_MENU))
        
        # Find and click the "Sign in" button
        sign_in_button = self.find_element(self.SIGN_IN_BUTTON_ON_MENU)
        # Use ActionChains to click the element
        ActionChains(self.driver).move_to_element(sign_in_button).click().perform()
        
    def enter_email(self, email):
        # Wait for the email input field to be visible
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        
        # Wait for the email input field to be clickable
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT))
        self.enter_text(self.EMAIL_INPUT, email)
        
    def click_continue2(self):
        self.click(self.CONTINUE_BUTTON2)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)
        
    def click_login(self):
        self.click(self.LOGIN_BUTTON)