#!/usr/bin/env python

# Unit test I/O

import sys
import signal
import board
import time
import RPi.GPIO as GPIO

SWITCH1_PIN = 23    # UVB Light
SWITCH2_PIN = 24    # Ceramic Light

RELAY1_PIN = 17 # UVB Light
RELAY2_PIN = 27 # Ceramic Light
RELAY3_PIN = 22 # Stage LED

def setup():



    GPIO.setmode(GPIO.BCM)

    GPIO.setup(SWITCH1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SWITCH2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    

    GPIO.setup(RELAY1_PIN, GPIO.OUT)
    GPIO.setup(RELAY2_PIN, GPIO.OUT)
    GPIO.setup(RELAY3_PIN, GPIO.OUT)

    GPIO.output(RELAY1_PIN, GPIO.LOW)
    GPIO.output(RELAY2_PIN, GPIO.LOW)
    GPIO.output(RELAY3_PIN, GPIO.LOW)


    return



def main():


    setup()


    while True:

        # Detect switch 1
        if GPIO.input(SWITCH1_PIN) == GPIO.LOW:
            print("Switch 1 pressed")
            GPIO.output(RELAY1_PIN, GPIO.HIGH)
        else:
            GPIO.output(RELAY1_PIN, GPIO.LOW)

        # Detect switch 2
        if GPIO.input(SWITCH2_PIN) == GPIO.LOW:
            print("Switch 2 pressed")
            GPIO.output(RELAY2_PIN, GPIO.HIGH)
        else:
            GPIO.output(RELAY2_PIN, GPIO.LOW)
        

        time.sleep(0.05)




    return


def signal_handler(sig, frame):
    print("Terminate program")
    GPIO.cleanup()
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()

