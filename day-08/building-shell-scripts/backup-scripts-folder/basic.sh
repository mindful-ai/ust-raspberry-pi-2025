#!/bin/bash

username=$(whoami)

echo "Welcome to the script!"
echo "Current user        -> $username"
echo "Current date        -> $(date)"
echo "Current working dir -> $(pwd)"
echo "Current shell       -> $SHELL"
#echo "Uptime              -> $(uptime -p)"