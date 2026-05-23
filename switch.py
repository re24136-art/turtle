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
    

    GPIO.setup(RELAY1_PIN, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(RELAY2_PIN, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(RELAY3_PIN, GPIO.OUT, initial=GPIO.HIGH)

    #GPIO.output(RELAY1_PIN, GPIO.LOW)
    #GPIO.output(RELAY2_PIN, GPIO.LOW)
    #GPIO.output(RELAY3_PIN, GPIO.LOW)


    return



def main():


    setup()

    UVB_STATE = GPIO.HIGH
    CERAMIC_STATE = GPIO.HIGH

    
    switch1_prev = GPIO.HIGH
    switch2_prev = GPIO.HIGH

    while True:

        switch1_now = GPIO.input(SWITCH1_PIN)
        switch2_now = GPIO.input(SWITCH2_PIN)


        # Detect switch 1
        if switch1_now == GPIO.LOW and switch1_prev == GPIO.HIGH:
            print("Switch 1 pressed")

            UVB_STATE = GPIO.HIGH if UVB_STATE == GPIO.LOW else GPIO.LOW
            GPIO.output(RELAY1_PIN, UVB_STATE)

        # Detect switch 2
        if switch2_now == GPIO.LOW and switch2_prev == GPIO.HIGH:
            print("Switch 2 pressed")

            CERAMIC_STATE = GPIO.HIGH if CERAMIC_STATE == GPIO.LOW else GPIO.LOW
            GPIO.output(RELAY2_PIN, CERAMIC_STATE)

        switch1_prev = switch1_now
        switch2_prev = switch2_now
        

        # Detect switch 2
        #if GPIO.input(SWITCH2_PIN) == GPIO.LOW:
        #    print("Switch 2 pressed")
        #    GPIO.output(RELAY2_PIN, GPIO.LOW)
        #else:
        #    GPIO.output(RELAY2_PIN, GPIO.HIGH)
     


        time.sleep(0.05)




    return


def signal_handler(sig, frame):
    print("Terminate program")
    GPIO.cleanup()
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()

