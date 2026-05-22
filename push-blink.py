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

        image = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjgiIGhlaWdodD0iMTI4Ij4KPHJlY3Qgd2lkdGg9IjY0IiBoZWlnaHQ9IjY0IiBmaWxsPSIjRkY1NzMzIi8+CjxyZWN0IHg9IjY0IiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIGZpbGw9IiMzM0M0RkYiLz4KPHJlY3QgeT0iNjQiIHdpZHRoPSI2NCIgaGVpZ2h0PSI2NCIgZmlsbD0iIzMzQ0Y3NyIvPgo8cmVjdCB4PSI2NCIgeT0iNjQiIHdpZHRoPSI2NCIgaGVpZ2h0PSI2NCIgZmlsbD0iI0ZGQ0YzMyIvPgo8dGV4dCB4PSI2NCIgeT0iNjQiIGZvbnQtc2l6ZT0iMTYiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZmlsbD0id2hpdGUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGRvbWluYW50LWJhc2VsaW5lPSJtaWRkbGUiPkRVTU1ZPC90ZXh0Pgo8L3N2Zz4="

        data = {
            "translucency_red":   translucency_red,
            "translucency_green": translucency_green,
            "translucency_blue":  translucency_blue,
            "camera_feed": image
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

