import os
from pprint import pprint
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import colorama

os.system("clear")


def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")


def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    responses = []
    for inputy in inputs:
        if inputy["type"] == "text" or inputy["type"] == "search":
            inputy["value"] = value
            input_name = inputy.get("name")
            input_value = inputy.get("value")
            if input_name and input_value:
                data[input_name] = input_value

            if form_details["method"] == "post":
                responses.append(requests.post(target_url, data=data))
            else:
                responses.append(requests.get(target_url, params=data))

    return responses


def scan_xss(url):
    XSS_list  = []
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        form_details = get_form_details(form)
        payload = "<script>alert('hello')</script>"
        responses = submit_form(form_details, url, payload)
        for response in responses:
            if payload in response.content.decode():
                XSS_list.append(str(form_details))
                print(colorama.Fore.RED + f"[!] XSS Detected on {url}")
                print(colorama.Fore.YELLOW + f"[*] Form details:" + colorama.Style.RESET_ALL)
                pprint(form_details)

    return XSS_list



if __name__ == "__main__":
    colorama.init()
    url = "https://demo.testfire.net/feedback.jsp"
    scan_xss(url)
    colorama.deinit()