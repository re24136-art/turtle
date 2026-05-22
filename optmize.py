#!/usr/bin/env python

import RPi.GPIO as GPIO
import board
import adafruit_dht
import time
import requests
import json


def change_fan_speed(fan, speed):
    fan.ChangeDutyCycle(speed)
    time.sleep(3)
    return


def push_data(token, data):

    url = f"http://thingsboard.cloud/api/v1/{token}/telemetry"

    resp = requests.post(url, json=data)
    print(resp)

    return


def calculate_optimum_speed(temperature, humidity):
    min_temp, max_temp = 32, 35
    min_humd, max_humd = 80, 85


    m1 = (100 - 50) / (max_temp - min_temp)
    c1 = 50 - m1*min_temp

    m2 = (100 - 50) / (max_humd - min_humd)
    c2 = 50 - m2*min_humd


    if temperature < min_temp:
        tspeed = 0
    elif temperature > max_temp:
        tspeed = 100
    else:
        tspeed = int(m1*temperature + c1)

    if humidity < min_humd:
        hspeed = 0
    elif humidity > max_humd:
        hspeed = 100
    else:
        hspeed = int(m2*humidity + c2)

    speed = max([tspeed, hspeed])

    print(f"temp:{temperature} humidity:{humidity} speed:{speed}")
    return speed


def load_key():
    with open("api.keys", 'r') as f:
        keys = json.load(f)
        return keys.get("thingsboard_token")

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


    key = load_key()


    while True:
        try:
            temperature = sensor.temperature
            humidity = sensor.humidity
        except Exception as e:
            print(f"DHT-11 error: {e}")
            continue

        fan_speed = calculate_optimum_speed(temperature, humidity)

        data = {
            "temperature": temperature,
            "humidity": humidity,
            "fan_speed": fan_speed
        }

        push_data(key, data)

        #print(temperature, humidity, speed)

        try:
            change_fan_speed(fan, fan_speed)
        except KeyboardInterrupt:
            fan.stop()
            GPIO.cleanup()
            return

        time.sleep(2.0)


    return


if __name__ == "__main__":
    main()

