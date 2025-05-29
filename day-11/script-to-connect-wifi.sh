#!/bin/bash

# Step 1: Rescan available Wi-Fi networks
nmcli device wifi rescan
sleep 2

# Step 2: Get the list of available networks sorted by signal strength
echo "Scanning for Wi-Fi networks..."
IFS=$'\n' read -d '' -r -a networks <<< "$(nmcli --terse --fields SSID,SIGNAL device wifi list | sort -t: -k2 -nr)"

# Step 3: Try connecting to the strongest known network
for entry in "${networks[@]}"; do
    ssid=$(echo "$entry" | cut -d':' -f1)

    # Skip empty SSIDs
    if [ -z "$ssid" ]; then
        continue
    fi

    echo "Trying to connect to: $ssid"

    # Check if we have a saved connection
    if nmcli connection show | grep -q "$ssid"; then
        nmcli connection up "$ssid" && echo "✅ Connected to $ssid" && exit 0
    else
        echo "❌ No saved password for $ssid, skipping..."
    fi
done

echo "❌ Could not connect to any known Wi-Fi network."
exit 1
