#!/usr/bin/env python

import requests
import json
import time
import random

def main():

    with open("blynk.keys", 'r') as f:
        keys = json.load(f)
        print(keys)

 
    url = f" https://blynk.cloud/external/api/update"

    while True:
        t_red = random.randint(80,90)

        params = {
            "token":keys.get('token'),
            "V4": str(t_red)
        }

        resp = requests.get(url, params)

        print(t_red, resp)
        time.sleep(3)

    return


if __name__ == "__main__":
    main()

