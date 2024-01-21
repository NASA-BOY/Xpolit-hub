import requests
from bs4 import BeautifulSoup
import sys

s = requests.session()
s.headers[
    "User agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"


def get_form(url):
    soup = BeautifulSoup(s.get(url).content, "html.parser")
    return soup.find_all("form")


def form_details(form):
    details_of_form = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get")
    inputs = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({
            "type": input_type,
            "name": input_name,
            "value": input_value,
        })

    details_of_form['action'] = action
    details_of_form['method'] = method
    details_of_form['inputs'] = inputs

    return details_of_form

def vulnerable(response):
    errors = {"quoted string not properly terminated",
              "unclosed quotation mark after the character string",
              "you have an error in you SQL syntax"
              }

    for error in errors:
        if error in response.content.decode().lower():
            return True
        return False


def sql_injection_scan(url):
    forms = get_form(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")

    for form in forms:
        details = form_details(form)

        for i in "\"'":
            data = {}
            for input_tag in details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    data[input_tag["name"]] = input_tag["value"] + i

                elif input_tag["type"] != "submit":
                    data[input_tag["name"]] = f"test{i}"


