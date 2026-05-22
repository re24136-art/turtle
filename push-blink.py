#!/usr/bin/env python

import requests
import json
import time
import random

def main():

    with open("api.keys", 'r') as f:
        keys = json.load(f)
        print(keys)

 
    #url = f" https://blynk.cloud/external/api/update"

    while True:
        translucency_red   = random.randint(80,90)
        translucency_green = random.randint(60,90)
        translucency_blue  = random.randint(40,60)


        data = {
            "translucency_red":   translucency_red,
            "translucency_green": translucency_green,
            "translucency_blue":  translucency_blue
        }

        #curl -v -X POST http://thingsboard.cloud/api/v1/3ghpxw6ekhfqc9tsmm1e/telemetry --header Content-Type:application/json --data "{temperature:25}"
        
        thingsboard_token = keys.get("thingsboard_token")

        url = f"http://thingsboard.cloud/api/v1/{thingsboard_token}/telemetry"
        #--header Content-Type:application/json --data "{temperature:25}"


        resp = requests.post(url, json=data)
        print(resp)

        time.sleep(10)
        return

    return


if __name__ == "__main__":
    main()


def blynk():
    pass
    """
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
    """

