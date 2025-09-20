import pytest
from pages.amazon_login_page import AmazonLoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

# Get the absolute path to the project root
project_root = os.path.abspath(os.path.dirname("E:\ecommerce_automation_framework\.env"))

# Construct the full path to the .env file
dotenv_path = os.path.join(project_root, '.env')

# Load variables from the .env file
# The verbose=True argument will print a message showing if the file was loaded
load_dotenv(dotenv_path, verbose=True)


# Get credentials from environment variables
TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")


def test_amazon_valid_login(driver):
    amazon_page = AmazonLoginPage(driver)

    # Step 0: Click continue
    amazon_page.click_continue1()

    # Step 1: Navigate to the sign-in page
    amazon_page.navigate_to_login()

    # Step 2: Enter email and click continue
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "ap_email_login"))
        )
    except Exception as e:
        pytest.fail(f"Login failed: Email field did not appear. Error: {e}")
    
    amazon_page.enter_email(TEST_EMAIL)
    amazon_page.click_continue2()

    # Step 3: Wait for the password field to be visible after the continue button is clicked
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "ap_password"))
        )
    except Exception as e:
        pytest.fail(f"Login failed: Password field did not appear. Error: {e}")

    # Step 4: Enter password and click sign-in
    amazon_page.enter_password(TEST_PASSWORD)
    amazon_page.click_login()


     # Assertion: Verify a successful login by checking for the "Hello, <YourName>" text
    try:
        WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element(
                (By.ID, "nav-link-accountList-nav-line-1"),
                "Hello,"
            )
        )
        print("Login successful: 'Hello,' element is present.")
    except Exception as e:
        pytest.fail(f"Login failed: 'Hello,' element not found. Error: {e}")