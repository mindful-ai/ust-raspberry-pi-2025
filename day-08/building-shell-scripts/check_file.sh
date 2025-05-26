#!/bin/bash

echo "Enter the name of the file to check: "
read filename

if [ -e "$filename" ]; then
    echo "The file $filename exists."
else
    echo "The file $filename does not exists."
fi  

