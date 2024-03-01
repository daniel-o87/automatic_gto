#!/bin/bash

echo "pot"
python pot_size.py 

convert image.png  -contrast-stretch 0% -colorspace Gray -density 300 output.tiff

tesseract output.tiff number --psm 7 > /dev/null 2>&1 
