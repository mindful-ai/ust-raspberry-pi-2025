#!/bin/bash

echo "Enter the directory name: "
read dirname

if [ -d "$dirname" ]; then
    echo "Listing the .sh file in the directory $dirname"
    for file in "$dirname"/*.sh;
    do 
        echo "$file"
    done
else
    echo "Directory $dirname does not exist"
fi