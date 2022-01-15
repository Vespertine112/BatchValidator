import requests
import os

# Author: Brayden Hill | Hillbgh@gmail.com

val_url = "https://validator.w3.org/nu/"

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
            response = requests.post(val_url, headers=headers, data=raw_html)

            parse_response = response.content

            if b"There were errors" in parse_response:
                print(item + " : Failed")
            else:
                print(item + " : Success")

    print("====== End ======")
