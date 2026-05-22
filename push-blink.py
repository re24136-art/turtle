#!/usr/bin/env python

import requests
import json


def main():

    with open("blynk.keys", 'r') as f:
        keys = json.load(f)
        print(keys)


    return


if __name__ == "__main__":
    main()

