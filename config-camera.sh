#!/usr/bin/bash

# Disable auto-exposure on webcam and manually set exposure
v4l2-ctl -d /dev/video0 --set-ctrl=auto_exposure=1,exposure_time_absolute=200
#,gain=128


# start preview
ffplay /dev/video0
