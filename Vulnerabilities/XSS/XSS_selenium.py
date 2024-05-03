import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from Vulnerabilities import scan_page

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException, NoAlertPresentException


def get_xss_payloads(file):
    with open(file, "r") as myfile:
        data = myfile.read().splitlines()
    return data


def scan_xss(forms_inputs, url):
    # get all the XSS payloads
    payloads = get_xss_payloads("payloads.txt")

    # Use Selenium to interact with the webpage
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)  # Replace with your preferred browser driver
    driver.get(url)

    for form in forms_inputs:
        if len(form["submit"]) > 0 and len(form["text"]) > 0:
            for payload in payloads:
                for input_txt in form["text"]:
                    # Type in payload to all the text inputs
                    input_type, value = input_txt
                    text_box = driver.find_element(input_type, value)
                    text_box.clear()
                    text_box.send_keys(payload)

                for submit_input in form["submit"]:
                    # Submit the payload by clicking the submit button
                    input_type, value = submit_input
                    submit_button = driver.find_element(input_type, value)
                    submit_button.click()

                try:
                    WebDriverWait(driver=driver, timeout=0.5).until(EC.alert_is_present())
                    alert = driver.switch_to.alert
                    alert.accept()

                    # # Get the page source
                    # page_source = driver.page_source
                    # print(page_source)
                    # if payload in page_source:
                    #     print("FOUND")
                    #     break
                    #
                    # else:
                    #     if driver.current_url != url:
                    #         driver.back()

                    print("found")
                    break

                except TimeoutException:
                    if driver.current_url != url:
                        driver.back()




url = "https://demo.testfire.net/feedback.jsp"
forms_inputs = scan_page.get_all_inputs(url)

scan_xss(forms_inputs, url)
