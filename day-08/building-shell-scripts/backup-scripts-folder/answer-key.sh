#!/bin/bash

# Ask for username
read -p "Enter username: " username

# Check if user exists in /etc/passwd
if id "$username" &>/dev/null; then
    echo "User '$username' exists." | tee user_report.log

    # Get home directory
    home_dir=$(eval echo ~$username)
    echo "Home directory: $home_dir" | tee -a user_report.log

    # Count running processes for user
    process_count=$(ps -u "$username" --no-headers | wc -l)
    echo "Number of running processes: $process_count" | tee -a user_report.log
else
    echo "User '$username' does not exist!" | tee user_report.log
fi
