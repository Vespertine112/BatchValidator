#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import glob

""" This script will validate all local directory html and css files against the w3c public API.
    It then prints a basic report to the console containing the success or failure of each validated file."""

__author__: "Brayden Hill"
__email__: "hillbgh@gmail.com"

url = "https://validator.w3.org/nu/"

def main():

    errors = {}

    directory = "./"
    pathname = directory + "/**/*.html"
    send_files = glob.glob(pathname, recursive=True)

    directory = "./"
    pathname = directory + "/**/*.css"
    send_files.extend(glob.glob(pathname, recursive=True))

    print("===== Report =====")

    for item in send_files:
        with open(item) as file:
            raw_html = file.read()

            # Update header for css or html validation
            if ".css" in item:
                headers = {'Content-type': 'text/css; charset=UTF-8', 'out': 'gnu'}
            else:
                headers = {'Content-type': 'text/html; charset=UTF-8', 'out': 'gnu'}

            response = requests.post(url, headers=headers, data=raw_html)
            response = response.content

            if b"There were errors" in response:
                print(f"{item} : \033[0;31mFailed\033[0m")
                errors[item] = response
            else:
                print(f"{item} : \033[0;32mSuccess\033[0m")
    print("====== End ======\n\n")

    if errors:
        parse_response_html(errors)


def parse_response_html(error_dict):
    for key in error_dict:
    # The key is the file name, the value is the response for the file.
        print(f"====== Errors within {key} ======")
        soup = BeautifulSoup(error_dict[key], "html.parser")

        all_errors = soup.find("div", id="results").find_all("p", {"class": None})
        locations = soup.find("div", id="results").find_all("p", {"class": "location"})

        for i in range(len(all_errors)):
            error = all_errors[i].text
            location = locations[i].text
            print(f"{error} \nLocation: {location}\n")
        print("\n\n")

if __name__ == '__main__':
    main()