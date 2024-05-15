import os


def get_sql_payloads(file):
    with open(file, "r") as myfile:
        data = myfile.read().splitlines()
    return data


def scan_sql(forms_inputs, url, driver):
    # List of the vulnerable forms index
    vuln_forms_index = []
    # Index for getting the form details
    index = 0

    # Get the directory path of the current Python script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    payloads_path = os.path.join(current_directory, "payloads.txt")

    # get all the XSS payloads
    payloads = get_sql_payloads(payloads_path)

    for form in forms_inputs:
        if len(form["submit"]) > 0 and len(form["text"]) > 0:
            for payload in payloads:

                while driver.current_url != url:
                    driver.back()

                for input_txt in form["text"]:
                    # Type in payload to all the text inputs
                    input_type, value = input_txt
                    text_box = driver.find_element(input_type, value)
                    text_box.clear()
                    text_box.send_keys(payload)

                for input_pass in form["password"]:
                    # Type in payload to all the text inputs
                    input_type, value = input_pass
                    text_box = driver.find_element(input_type, value)
                    text_box.clear()
                    text_box.send_keys(payload)

                for submit_input in form["submit"]:
                    # Submit the payload by clicking the submit button
                    input_type, value = submit_input
                    submit_button = driver.find_element(input_type, value)
                    submit_button.click()

                try:
                    # Get the page source
                    page_source = driver.page_source
                    print(page_source)
                    if "error" in page_source:
                        vuln_forms_index.append(index)
                        break

                except:
                    pass

        # Increase the index for the next run
        index += 1

    # Return True for vulnerable if the vulnerable forms list is not empty and return the list
    return len(vuln_forms_index) > 0, vuln_forms_index

#
# url = "http://localhost/dvwa/vulnerabilities/sqli/"
# cookiess = get_cookies.load_cookies_from_string()
# forms_inputs = scan_page.get_all_inputs(url, cookiess)
#
# scan_sql(forms_inputs, url, cookiess)
