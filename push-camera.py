#!/usr/bin/env python

import cv2

import requests
import json
import time
import random
import base64


def capture_turtle():
    cam = cv2.VideoCapture(0)
    flag, frame = cam.read()
    cam.release()

    if not flag:
        print("Camera KO")
        return None

    print(frame.shape)

    # Resize image
    scale = 0.25
    height = int(frame.shape[0] * scale)
    width  = int(frame.shape[1] * scale)

    frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

    _, image = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])

    if not _:
        print("Compression KO")
        return None

    image64 = base64.b64encode(image).decode('utf-8')
    print(image64)

    return f"data:image/jpeg;base64,{image64}"



def main():

    with open("api.keys", 'r') as f:
        keys = json.load(f)
        print(keys)
        thingsboard_token = keys.get("thingsboard_token")


    while True:

        image = capture_turtle()
        if image is None: continue

        data = { "camera_feed": image }

        url = f"http://thingsboard.cloud/api/v1/{thingsboard_token}/attributes"

        resp = requests.post(url, json=data)
        print(resp)

        time.sleep(5)


    return


if __name__ == "__main__":
    main()


