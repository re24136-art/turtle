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
        t_r = random.randint(80,90)
        t_g = random.randint(80,90)
        t_b = random.randint(80,90)

        params = { "token":keys.get('token'), "V4": str(t_r) }
        resp_r = requests.get(url, params)
        time.sleep(1)


        params = { "token":keys.get('token'), "V5": str(t_g) }
        resp_g = requests.get(url, params)
        time.sleep(1)

        params = { "token":keys.get('token'), "V6": str(t_b) }
        resp_b = requests.get(url, params)
        time.sleep(1)


        print(t_r, t_g, t_b)
        print(resp_r, resp_g, resp_b)

        time.sleep(10)

    return


if __name__ == "__main__":
    main()

