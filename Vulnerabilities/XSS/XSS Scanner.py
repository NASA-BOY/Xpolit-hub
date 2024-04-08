import colorama
import requests
import time
import sys
from colorama import Fore, Back, Style

# hack_in_the... XSS scanner

colorama.init()
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
print(Fore.GREEN + "XSS SCANNER" + Fore.RED + "Xploit Hub" + Style.RESET_ALL)
time.sleep(2)
print()

pog = input("POST ot GET? (p/g): ")
if pog == 'g':
    try:
        site = input("Enter URL: ")
        r = requests.post(site, headers=header, verify=False)
        time.sleep(1)
        print()
        print(Fore.GREEN + "The site respond! " + Style.RESET_ALL)

    except:
        print()
        print("does the script responds?")
        time.sleep(3)
        print()
        print(Fore.RED + "The site doesn't respond, try again." + Style.RESET_ALL)
        sys.exit(0)

    print()

    try:
        payloads_dir = "/payloads/xss_payloads.txt"
        reper = open(payloads_dir, "r")

    except FileNotFoundError:
        print()
        print("The File " + Fore.RED + payloads_dir + Style.RESET_ALL + "Doesn't exist!")
        sys.exit(0)

    print()
    print(Fore.GREEN + "Test in progress...\n")
    time.sleep(2)
    payloads = open(payloads_dir, "r")
    l = 1
    for payload in payloads:

        if payload in requests.get(site + payload, headers=header).text:
            print(Fore.RED + "XSS FOUND " + Style.RESET_ALL)
            print(requests.get(site + payload, headers=header).url)

        else:
            print(Fore.RED + "Site is secure" + Style.RESET_ALL)
            l += 1
