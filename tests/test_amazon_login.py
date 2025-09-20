import pytest
from pages.amazon_login_page import AmazonLoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Get credentials from environment variables
TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")

def test_amazon_valid_login(driver):
    amazon_page = AmazonLoginPage(driver)

    # Step 1: Navigate to the sign-in page
    amazon_page.navigate_to_login()

    # Step 2: Enter email and click continue
    amazon_page.enter_email("TEST_EMAIL") # Use a valid, real email
    amazon_page.click_continue()

    # Step 3: Enter password and click sign-in
    # You may have to handle a 2FA prompt here
    amazon_page.enter_password("TEST_PASSWORD") # Use a valid, real password
    amazon_page.click_login()

     # Assertion: Verify a successful login by checking for the "Hello, <YourName>" text
    try:
        WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element(
                (By.ID, "nav-link-accountList-nav-line-1"),
                "Hello, Saurabh" # Replace with a known part of the text
            )
        )
        print("Login successful: 'Hello, Saurabh' element is present.")
    except Exception as e:
        pytest.fail(f"Login failed: 'Hello, Saurabh' element not found. Error: {e}")