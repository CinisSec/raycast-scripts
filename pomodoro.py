#!/usr/bin/env python3
import subprocess
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title pomodoro
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🍅
# @raycast.argument1 { "type": "text", "placeholder": "6" }
# @raycast.packageName time

# Documentation:
# @raycast.description pomodoro timer
# @raycast.author Grey

import sys 
import time 
import math

timer = int(sys.argv[1])

if len(sys.argv) == 2:
    if timer > 5:
        time.sleep(timer * 60)
        rest_time = timer / 5
        rest_time_str = str(math.floor(rest_time))
        # opens a MacOS dialog
        subprocess.run(["osascript",
                        "-e",
                        'display dialog "Time to take a break for ' + rest_time_str + ' minutes!" with title "Break time!" with icon POSIX file "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/AlertStopIcon.icns" buttons {"OK"}'
                        ])
    else:
        print("No microdosing focus here buddy, give it more than 5 minutes.")

else:
    print("Usage: pomodoro.py <time in minutes 5min >")







