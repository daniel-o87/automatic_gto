#!/bin/bash

FILENAME="$1"
echo "pot"
python pot_size.py "$FILENAME"

convert pot_size.png -colorspace Gray -contrast-stretch 0% -threshold 50% output.tiff

tesseract output.tiff number --oem 2 --psm 7 > /dev/null 2>&1 
