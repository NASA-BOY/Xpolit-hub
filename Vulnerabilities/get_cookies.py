import json


def load_cookies_from_string(cookies_str):
    # Parse cookies string into a list of dictionaries
    cookies = json.loads(cookies_str)

    # Convert list of dictionaries into a single dictionary with cookie names as keys
    cookies_dict = {cookie["name"]: cookie["value"] for cookie in cookies}
    return cookies_dict

