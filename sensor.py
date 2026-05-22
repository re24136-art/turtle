#!/usr/bin/env python

import board
import adafruit_dht
import time


def main():


    sensor = adafruit_dht.DHT11(board.D4)

    while True:
        try:
            print(sensor.temperature)
            pass
        except Exception as e:
            print(e)
            pass
        time.sleep(2.0)


    return


if __name__ == "__main__":
    main()

