import time

from selenium import webdriver
import requests

from Vulnerabilities import get_cookies

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup

# Define the URL of your website
url = "http://localhost/dvwa/vulnerabilities/csrf/"

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get(url)

cookies = get_cookies.load_cookies_from_string()

for name, value in cookies.items():
    cookie = {'name': name, 'value': value}
    driver.add_cookie(cookie)

    # Refresh the page to apply the cookies
    driver.refresh()

    driver.get(url)

try:
    # Wait for the forms to be present on the page
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "form")))

    # Find all forms on the webpage
    forms = driver.find_elements(By.TAG_NAME, 'form')

    # Check each form for CSRF vulnerability
    for form in forms:
        form_data = {}
        form_action = form.get_attribute('action')
        method = form.get_attribute('method').upper() or 'GET'

        # Collect form input data
        for input_element in form.find_elements(By.TAG_NAME, 'input'):
            name = input_element.get_attribute('name')
            value = input_element.get_attribute('value')
            if name:
                form_data[name] = value

        # Attempt to submit the form without authentication
        try:
            # Send a request without authentication
            response = requests.request(method, url + form_action, data=form_data)

            # If the request was successful without requiring authentication, it indicates a potential CSRF vulnerability
            if response.status_code == 200:
                print(f"Potential CSRF vulnerability found in form: {form_action}")
        except Exception as e:
            print(f"Error occurred while checking form {form_action}: {e}")

except Exception as e:
    print(f"Error occurred while processing the page: {e}")

# Close the WebDriver
driver.quit()
