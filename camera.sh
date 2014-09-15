#!/usr/bin/env sh
mjpg_streamer -i "input_uvc.so -r 352x288 -f 8" -o "output_http.so -w /usr/share/mjpeg-streamer/www/"

