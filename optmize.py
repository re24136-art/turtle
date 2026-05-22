#!/usr/bin/env python

import RPi.GPIO as GPIO
import board
import adafruit_dht
import time


def change_fan_speed(fan, speed):
    fan.ChangeDutyCycle(speed)
    time.sleep(3)
    return


def calculate_optimum_speed(temperature, humidity):
    min_temp, max_temp = 32, 35
    min_humd, max_humd = 80, 85


    m1 = (100 - 50) / (max_temp - min_temp)
    c1 = 50 - m1*min_temp

    if temperature < min_temp:
        tspeed = 0
    elif temperature > max_temp:
        tspeed = 100
    else:
        tspeed = int(m1*temperature + c1)


    speed = tspeed
    print(f"temp:{temperature} speed:{speed}")
    return speed




def main():

    # Init sensor
    sensor = adafruit_dht.DHT11(board.D4)

    # Set PWM pin
    FAN_PIN = 18
    PWM_FREQ = 25 # Hz

    # Init PWM pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT)
    fan = GPIO.PWM(FAN_PIN, PWM_FREQ)

    # Zero pulse
    fan.start(0)


    while True:
        try:
            temperature = sensor.temperature
            humidity = sensor.humidity
        except Exception as e:
            print(f"DHT-11 error: {e}")
            continue

        speed = calculate_optimum_speed(temperature, humidity)
        #print(temperature, humidity, speed)

        try:
            change_fan_speed(fan,speed)
        except KeyboardInterrupt:
            fan.stop()
            GPIO.cleanup()
            return

        time.sleep(1.0)


    return


if __name__ == "__main__":
    main()

