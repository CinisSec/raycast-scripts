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

battery_level = psutil.sensors_battery().percent
print(str(battery_level) + "%")

