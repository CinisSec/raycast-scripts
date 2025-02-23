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
            return location, "OK"
        case "rotterdam":
            subprocess.run(["open", "-a", "Safari", "https://www.buienalarm.nl/nederland/rotterdam/16707"])
            return location, "OK"
        case "brussels":
            subprocess.run(["open", "-a", "Safari", "https://www.buienalarm.nl/belgie/brussels/7196"])
            return location, "OK"
        case "antwerp":
            subprocess.run(["open", "-a", "Safari", "https://www.buienalarm.nl/belgie/antwerpen/5686"])
            return location, "OK"

loc = sys.argv[1]
open_safari(loc.lower())


