#!/bin/bash


mkdir -p backup-scripts-folder

#for file in $(ls *.sh); 
for file in *.sh;
do 
    if [ -f "$file" ]; then
        cp "$file" backup-scripts-folder
        echo "Backed up $file to backup-scripts-folder/"
    fi
done