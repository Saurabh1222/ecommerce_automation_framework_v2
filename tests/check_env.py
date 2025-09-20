# check_env.py
import os
from dotenv import load_dotenv

# Get the absolute path to the project root
project_root = os.path.abspath(os.path.dirname("E:\ecommerce_automation_framework\.env"))

# Construct the full path to the .env file
dotenv_path = os.path.join(project_root, '.env')

# Load variables from the .env file
# The verbose=True argument will print a message showing if the file was loaded
load_dotenv(dotenv_path, verbose=True)

# Retrieve the variables and print them
test_email = os.getenv("TEST_EMAIL")
test_password = os.getenv("TEST_PASSWORD")

print(f"TEST_EMAIL from .env: {test_email}")
print(f"TEST_PASSWORD from .env: {test_password}")