#!/bin/bash
echo "pot"
python pot_size.py 

convert image.png  -contrast-stretch 0% -colorspace Gray -morphology Convolve Gaussian:0x1 -sharpen 0x3 -level 20%,80% -negate -units PixelsPerInch -density 300  output.tiff

tesseract output.tiff number --psm 7 > /dev/null 2>&1 

python3 update.py
