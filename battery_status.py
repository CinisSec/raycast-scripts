#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title battery_status
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🔋
# @raycast.packageName psutil

# Documentation:
# @raycast.description check battery status
# @raycast.author Grey

import psutil

def get_battery_status():
    battery_level = psutil.sensors_battery().percent
    return battery_level

print(str(get_battery_status()) + "%")