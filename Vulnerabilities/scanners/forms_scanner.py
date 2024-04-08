import requests
from bs4 import BeautifulSoup as bs


def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

print(get_all_forms("https://demo.testfire.net/login.jsp"))
