#!/usr/bin/bash

v4l2-ctl -d /dev/video0 --set-ctrl=auto_exposure=1,exposure_time_absolute=250
#,gain=128
