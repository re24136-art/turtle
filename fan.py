#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def change_speed(fan, speed):
    print("Speed", speed)
    fan.ChangeDutyCycle(speed)
    time.sleep(3)
    return

def main():

    #GPIO.cleanup()
    #return

    FAN_PIN = 18
    PWM_FREQ = 25 # Hz

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT)

    fan = GPIO.PWM(FAN_PIN, PWM_FREQ)
    fan.start(0)

    for speed in range(40, 100, +10):
        change_speed(fan,speed)

    time.sleep(5)

    for speed in range(100, 40-1, -10):
        change_speed(fan,speed)


    #try:
    #    pass
    #except KeyboardInterrupt:
    #    fan.stop()
    #    GPIO.cleanup()
    

    fan.stop()
    GPIO.cleanup()

    return


if __name__ == "__main__":
    main()

