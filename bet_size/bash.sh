#!/bin/bash

WORKDIR="/home/do/Desktop/fun_testing/automatic_gto/bet_size"
NEWDIR="/home/do/Desktop/fun_testing/automatic_gto/ml_cards"


cd "$WORKDIR"

rm -f *.png *.txt *.tiff

FILENAME="$1"
echo "bet_size"

cd "$NEWDIR && ./players.sh"

python3 bet_size.py 

for file in *testing.png; do
    base_name="${file%testing.png}"

    output_tiff="${base_name}tiff"
    output_txt="${base_name}"

    convert "$file" -contrast-stretch 0% -colorspace Gray -sharpen 0x3 -level 20%,80% -units PixelsPerInch -density 300 "$output_tiff"
#-morphology Convolve Gaussian:0x1  -negate
    tesseract "$output_tiff" "$output_txt" --psm 7 > /dev/null 2>&1
done

python3 update.py
