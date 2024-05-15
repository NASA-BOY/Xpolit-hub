import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException, NoAlertPresentException


def get_xss_payloads(file):
    with open(file, "r") as myfile:
        data = myfile.read().splitlines()
    return data


def scan_xss(forms_inputs, url, driver):
    # List of the vulnerable forms index
    vuln_forms_index = []
    # Index for getting the form details
    index = 0

    # Get the directory path of the current Python script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    payloads_path = os.path.join(current_directory, "payloads.txt")

    # get all the XSS payloads
    payloads = get_xss_payloads(payloads_path)

    for form in forms_inputs:
        if len(form["submit"]) > 0 and len(form["text"]) > 0:
            for payload in payloads:

                # Make sure that the original page is open
                if driver.current_url != url:
                    driver.get(url)

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
                    vuln_forms_index.append(index)
                    break

                except TimeoutException:
                    pass

        # Increase the index for the next run
        index += 1


    # Return True for vulnerable if the vulnerable forms list is not empty and return the list
    return len(vuln_forms_index) > 0, vuln_forms_index

#
# url = "https://demo.testfire.net/feedback.jsp"
#
# forms_inputs = scan_page.get_all_inputs(url)
#
# # Use Selenium to interact with the webpage
# options = webdriver.ChromeOptions()
# # options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)  # Replace with your preferred browser driver
# driver.get(url)
#
# cookies = get_cookies.load_cookies_from_string()
#
# if cookies is not None:
#     # Add each cookie to the WebDriver
#     for name, value in cookies.items():
#         cookie = {'name': name, 'value': value}
#         driver.add_cookie(cookie)
#
#     # Refresh the page to apply the cookies
#     driver.refresh()
#
#     driver.get(url)
#
#
# scan_xss(forms_inputs=forms_inputs, url=url, driver=driver)
