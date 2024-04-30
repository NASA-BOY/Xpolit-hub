import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin


# Specify the website URL
url = "https://demo.testfire.net/login.jsp"

# Use Selenium to interact with the webpage
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)  # Replace with your preferred browser driver
driver.get(url)

for i in range(1, 50):
    # Define the text you want to enter (adjust based on the website)
    text_to_enter = "admi"

    # Identify the element where you want to enter the text (use browser developer tools)
    text_box = driver.find_element("id", "uid")  # Replace with actual ID
    text_box.send_keys(text_to_enter)
    text_box = driver.find_element("id", "passw")  # Replace with actual ID
    text_box.send_keys(text_to_enter)

    # Identify the submit button element (use browser developer tools)
    submit_button = driver.find_element("name", "btnSub")  # Replace with actual ID
    submit_button.click()

    # # Retrieve the website's response (HTML content)
    # response_text = driver.page_source
    #
    # # Print the response to the console
    # print(response_text)

    print(driver.current_url)

# Close the browser
driver.quit()
