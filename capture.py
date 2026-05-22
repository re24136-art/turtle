#!/usr/bin/env python

import cv2
import numpy as np
import time
from datetime import datetime

def capture_turtle():
    cam = cv2.VideoCapture(0)
    time.sleep(1)

    flag, frame = cam.read()

    if not flag:
        print("KO")
        cam.release()
        return None

    # Save image
    print("OK")
 
    cropY, cropX = 150, 200
    size = 200

    # Crop
    frame = frame[cropY:cropY+size, cropX:cropX+size, :]

    cam.release()

    return frame


def calculate_info(frame):
    # Extract RGB (openCV convention)
    print(frame.shape)
    frameR = frame[:,:,2]
    frameG = frame[:,:,1]
    frameB = frame[:,:,0]

    # Calculate mean and std.dev for each channel
    meanR = np.mean(frameR)
    meanG = np.mean(frameG)
    meanB = np.mean(frameB)

    std_devR = np.std(frameR)
    std_devG = np.std(frameG)
    std_devB = np.std(frameB)

    print(f"Mean channel R: {meanR:.2f}")
    print(f"Mean channel G: {meanG:.2f}")
    print(f"Mean channel B: {meanB:.2f}")

    print()
    print(f"Std.dev. channel R: {std_devR:.2f}")
    print(f"Std.dev. channel G: {std_devG:.2f}")
    print(f"Std.dev. channel B: {std_devB:.2f}")

    cv2.imwrite(f"channelR.jpg", frameR)
    cv2.imwrite(f"channelG.jpg", frameG)
    cv2.imwrite(f"channelB.jpg", frameB)
    return





def main():

    while True:
        now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        fname = f"lapse/{now}.jpg"

        frame = capture_turtle()
        if frame is None: continue
        print(now)
        cv2.imwrite(fname, frame)

        #calculate_info(frame)
        time.sleep(3)

    return


if __name__ == "__main__":
    main()

