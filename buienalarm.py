#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title buienalarm
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🌧️
# @raycast.argument1 { "type": "text", "placeholder": "Delft" }

# Documentation:
# @raycast.author Grey

import sys
import subprocess

def open_safari(location):
    match location:
        case "delft":
            subprocess.run(["open", "-a","Safari", "https://www.buienalarm.nl/nederland/delft/8569"])
            return "OK"
        case "rotterdam":
            subprocess.run(["open", "-a", "Safari", "https://www.buienalarm.nl/nederland/rotterdam/16707"])
            return "OK"
        case "brussels":
            subprocess.run(["open", "-a", "Safari", "https://www.buienalarm.nl/belgie/brussels/7196"])
            return "OK"
        case "antwerp":
            subprocess.run(["open", "-a", "Safari", "https://www.buienalarm.nl/belgie/antwerpen/5686"])
            return "OK"
        case _:
            return "ERROR_INVALID_LOCATION"

if len(sys.argv) > 1:
    loc = sys.argv[1]
    ecode = open_safari(loc.lower())
    print(ecode)
else:
    print("Usage: buienalarm.py <location>")
    print("Available location: delft, rotterdam, brussels, antwerp")



