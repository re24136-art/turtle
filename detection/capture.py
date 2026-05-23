#!/usr/bin/env python

# Unit test for object detection and trigger relay for LED

import imageio
import cv2
import numpy as np
import time
from datetime import datetime

import signal
import sys
import RPi.GPIO as GPIO

RELAY3_PIN = 22 # Stage LED


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY3_PIN, GPIO.OUT, initial=GPIO.HIGH)
    return


def capture_image():
    cam = cv2.VideoCapture(0)

    flag, frame = cam.read()

    if not flag:
        print("Camera KO")
        cam.release()
        return None

    # Save image
    #print("OK")
 
    cropY, cropX = 0, 0
    size = 400

    # Crop
    frame = frame[cropY:cropY+size, cropX:cropX+size, :]

    cam.release()

    return frame


# For calibration
def capture_background():

    NT = 5
    #bg = np.zeros((480, 640,3), dtype=np.float128)
    bg = np.zeros((400, 400,3), dtype=np.float128)

    for t in range(NT):
        print(t)
        frame = capture_image()
        if frame is None: continue

        bg += frame / 255.


        time.sleep(1)
    img = bg/float(NT)*255.0
    img = img.astype(np.uint8)

    cv2.imwrite("background.bmp", img)
    return


# Handle program termination
def signal_handler(sig, frame):
    print("Terminate program")
    GPIO.cleanup()
    sys.exit(0)


def main():

    setup()

    #capture_background()
    #return

    bg = imageio.imread("background.bmp")
    bg = bg[:,:,0].astype(np.float64)/255.0

    #print(bg)


    #return

    while True:
        now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        fname = f"lapse/{now}.jpg"

        frame = capture_image()
        if frame is None: continue


        f = frame[:,:,2].astype(np.float64)/255.0

        #cv2.imwrite("frame.png", (f*255).astype(np.uint8))
        #obj = (1-f) - (1-bg)
        #obj = 1 - obj + 0.1

        obj = np.abs(f-bg)

        score = np.mean(obj) * 255.0
        print(score)

        if score > 5.0:
            # pass
            print("Object detected")

            GPIO.output(RELAY3_PIN, GPIO.LOW)
        else:
            GPIO.output(RELAY3_PIN, GPIO.HIGH)



        #obj = (obj*255).astype(np.uint8)


        #print(frame.shape, frame.dtype)

        #cv2.imshow("ti",obj)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        #print(now)
        #cv2.imwrite(fname, frame)

        #calculate_info(frame)
        time.sleep(2.0)

    return


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()

