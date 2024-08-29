#!/bin/bash
python3 /home/pi/project/v1/get_battery_file.py
python /home/pi/project/v1/diagnostics_to_display.py 
python3 /home/pi/project/v1/fetch_photo.py
python /home/pi/project/v1/photo_to_display.py
