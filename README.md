# ﻿Automated E-commerce Testing Framework
This project is an automated end-to-end testing framework for an e-commerce website, designed to validate key functionalities from user registration to checkout. The framework is built with Python and Selenium, following best practices for maintainability and scalability.
# Technologies Used
* Python: The core programming language for the test scripts.
* Selenium WebDriver: For automating browser interactions.
* pytest: The testing framework for running tests and managing test cases.
* Page Object Model (POM): A design pattern to create a maintainable and reusable test suite by separating the test logic from the page elements.
* Allure Reports: A powerful reporting tool for generating comprehensive and interactive test reports.
# Features
- Page Object Model (POM): The framework uses POM to organize the code. Each web page (e.g., Login Page) has a corresponding class that contains its web elements and methods for interacting with them. This ensures that if a UI element changes, only one file needs to be updated.
- Data-Driven Testing: Test scenarios are data-driven, allowing for the execution of multiple test cases with different data sets (e.g., testing with various user credentials).
- Comprehensive Reporting with Allure: The framework generates detailed and visually appealing test reports using Allure. These reports provide a clear overview of test results, including test steps, attachments (like screenshots), and test execution timelines.
# Prerequisites
- Python 3.x installed
- A web browser (e.g., Google Chrome)
- A virtual environment (recommended)
# Project Structure
The framework is organized to be modular and easy to navigate:

├── 📁 test_cases

│ ├── 📝 test_login.py

├── 📁 pages

│ ├── 📝 base_page.py

├── 📁 reports

│ └── 📁 allure-results

├── 📄 requirements.txt

# 🚀 Getting Started

## 1. Clone the Repository
```bash
git clone <your-repository-url>
cd <your-repository-name>
```
# 2. Install dependencies
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Install the required libraries
pip install -r requirements.txt
```
#  3. Run the Tests
To run the entire test suite and generate the Allure report, use the following command:
```
pytest --alluredir=./reports/allure-results
```
This will execute all tests and save the results in the reports/allure-results directory.
# 4. View the Allure Report
After the tests have run, generate the HTML report and serve it locally:
```allure serve ./reports/allure-results```
The report will automatically open in your browser.




