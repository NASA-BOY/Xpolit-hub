import pprint
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

accepted_input_types = ["text", "submit", "password"]


def get_all_forms(url, cookies):
    soup = bs(requests.get(url, cookies=cookies).content, "html.parser")
    return soup.find_all("form")


def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_id = input_tag.attrs.get("id")
        input_value = input_tag.attrs.get("value")
        if input_type in accepted_input_types:
            inputs.append({"type": input_type, "name": input_name, "id": input_id, "value": input_value})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return inputs, pprint.pformat(details)


def get_all_inputs(url, cookies=None):
    forms = get_all_forms(url, cookies)
    # A list of all the inputs. Each item on the list is a form, inside of it is a dictionary of the type of input and
    # all of the ids of that input type.
    forms_inputs = []
    forms_details = []
    for form in forms:
        inputs, details = get_form_details(form)
        forms_details.append(details)
        form_inputs = {}

        # Add all the accepted input types to the dictionary of inputs as a list for this type of input
        for accepted_input in accepted_input_types:
            form_inputs[accepted_input] = []

        for input_obj in inputs:
            if input_obj["name"] is not None:
                form_inputs[input_obj["type"]].append((By.NAME, input_obj["name"]))
            elif input_obj["id"] is not None:
                form_inputs[input_obj["type"]].append((By.ID, input_obj["id"]))
            elif input_obj["value"] is not None:
                value = input_obj["value"]
                form_inputs[input_obj["type"]].append((By.CSS_SELECTOR, f"[value='{value}']"))

        forms_inputs.append(form_inputs)

    print(forms_inputs)
    return forms_inputs, forms_details

