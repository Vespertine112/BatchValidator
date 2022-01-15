#!/usr/bin/env python
import os

import requests

""" This script will validate all local directory html and css files against the w3c public API.
    It then prints a basic report to the console containing the success or failure of each validated file."""

__author__: "Brayden Hill"
__email__: "hillbgh@gmail.com"

url = "https://validator.w3.org/nu/"

if __name__ == '__main__':
    local_dir = os.getcwd()
    local_files = os.listdir(local_dir)
    send_files = []

    for name in local_files:
        if ".html" in name or ".css" in name:
            send_files.append(name)

    print("===== Report =====")

    for item in send_files:
        with open(item) as file:
            raw_html = file.read()
            headers = {'Content-type': 'text/html; charset=UTF-8', 'out': 'gnu'}
            response = requests.post(url, headers=headers, data=raw_html)

            parse_response = response.content

            if b"There were errors" in parse_response:
                print(item + " : Failed")
            else:
                print(item + " : Success")

    print("====== End ======")
