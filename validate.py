#!/usr/bin/env python
import os

import requests
from bs4 import BeautifulSoup

""" This script will validate all local directory html and css files against the w3c public API.
    It then prints a basic report to the console containing the success or failure of each validated file."""

__author__: "Brayden Hill"
__email__: "hillbgh@gmail.com"

url = "https://validator.w3.org/nu/"

def main():
    local_dir = os.getcwd()
    local_files = os.listdir(local_dir)
    send_files = []
    errors = {}

    for name in local_files:
        if ".html" in name or ".css" in name:
            send_files.append(name)

    print("===== Report =====")

    for item in send_files:
        with open(item) as file:
            raw_html = file.read()
            headers = {'Content-type': 'text/html; charset=UTF-8', 'out': 'gnu'}
            response = requests.post(url, headers=headers, data=raw_html)

            response = response.content

            if b"There were errors" in response:
                print(f"{item} : Failed")
                errors[item] = response
            else:
                print(f"{item} : Success")
    print("====== End ======\n\n")

    if errors:
        parse_response_html(errors)


def parse_response_html(error_dict):
    for key in error_dict:
        print(f"====== Errors within {key} ======")
        soup = BeautifulSoup(error_dict[key], "html.parser")
        all_errors = soup.find("div", id="results").find_all("p", {"class": None})
        for error in all_errors:
            error = error.text
            print(error)
        print("\n\n")

if __name__ == '__main__':
   main()
