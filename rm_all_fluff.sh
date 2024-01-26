#!/bin/bash
#RUNNING THIS WILL REMOVE ALL CREATED TXT, PNG, AND TIFF FILES EXCEPT player_status.txt

# Find and delete all .txt, .png, and .tiff files except player_status.txt and files in 'arbitrary' and 'full_img' directories
find . -type f \( -name "*.txt" -o -name "*.png" -o -name "*.tiff" \) ! -name "player_status.txt" ! -name "game.txt" -not \( -path "./arbitrary/*" -o -path "./full_img/*" \) -exec rm {} +
