#!/bin/bash
#RUNNING THIS WILL REMOVE ALL CREATED TXT AND PNG FILES
find . -type f \( -name "*.txt" -o -name "*.png" -o -name "*.tiff" \) -not \( -path "./arbitrary/*" -o -path "./full_img/*" \) -exec rm {} +
