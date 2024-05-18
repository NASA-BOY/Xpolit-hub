import time
import builtwith
import Vulnerabilities.Command_Injection.payloads as pay


def scan_cmd_injection(forms_inputs, url, driver):
    # List of the vulnerable forms index
    vuln_forms_index = []
    # Index for getting the form details
    index = 0

    try:
        for form in forms_inputs:
            if len(form["submit"]) > 0 and len(form["text"]) > 0:

                try:
                    # Check what is the operating system
                    info = builtwith.parse(url)
                    op_system = info["operating-systems"]
                    if op_system == ['Windows Server']:
                        payloads = pay.win_payloads
                    else:
                        payloads = pay.unix_payloads

                # If unable to find out the website operating system then try for both
                except KeyError:
                    payloads = pay.win_payloads + pay.unix_payloads

                for payload in payloads:

                    # Separate the command payload and the corresponding response for that command
                    cmd_payload, response = payload

                    # Make sure that the original page is open
                    if driver.current_url != url:
                        driver.get(url)

                    for input_txt in form["text"]:
                        # Type in payload to all the text inputs
                        input_type, value = input_txt
                        text_box = driver.find_element(input_type, value)
                        text_box.clear()
                        text_box.send_keys(cmd_payload)

                    for submit_input in form["submit"]:
                        # Submit the payload by clicking the submit button
                        input_type, value = submit_input
                        submit_button = driver.find_element(input_type, value)
                        submit_button.click()

                    try:
                        # Get the page source
                        page_source = driver.page_source
                        print(page_source)
                        if response in page_source:
                            vuln_forms_index.append(index)
                            break

                    except:
                        pass

            # Increase the index for the next run
            index += 1
    except Exception as e:
        print(e)

    # Return True for vulnerable if the vulnerable forms list is not empty and return the list
    return len(vuln_forms_index) > 0, vuln_forms_index

#
# # ======================================
#
# url = "http://127.0.0.2/dvwa/vulnerabilities/exec/"
#
# # Use Selenium to interact with the webpage
# options = webdriver.ChromeOptions()
# # options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)  # Replace with your preferred browser driver
# driver.get(url)
#
# cookies_str = """
#     [
# {
#     "domain": "127.0.0.2",
#     "expirationDate": 1715641612.847073,
#     "hostOnly": true,
#     "httpOnly": true,
#     "name": "PHPSESSID",
#     "path": "/",
#     "sameSite": "strict",
#     "secure": false,
#     "session": false,
#     "storeId": "0",
#     "value": "km24bjtlg2ntpir2u00aehus5q",
#     "id": 1
# },
# {
#     "domain": "127.0.0.2",
#     "hostOnly": true,
#     "httpOnly": true,
#     "name": "security",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": false,
#     "session": true,
#     "storeId": "0",
#     "value": "impossible",
#     "id": 2
# }
# ]
#     """
#
# cookies = get_cookies.load_cookies_from_string(cookies_str)
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
# forms_inputs = scan_page.get_all_inputs(url, cookies)
#
# scan_cmd_injection(forms_inputs=forms_inputs, url=url, driver=driver)
