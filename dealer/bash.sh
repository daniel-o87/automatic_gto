#!/bin/bash

rm *.txt *.png *.tiff
FILENAME="$1"

python test.py

for file in *testing.png; do
      base_name=$(echo "$file" | sed 's/testing.png//')

    # Define the output filenames for the TIFF and text files
    output_tiff="${base_name}.tiff"
    output_txt="${base_name}"

	convert "$file" -contrast-stretch 0% -colorspace Gray -morphology Convolve Gaussian:0x1 -sharpen 0x3 -level 20%,80% -negate -units PixelsPerInch -density 300 "$output_tiff"

        # Run Tesseract OCR on the preprocessed TIFF file to extract text
    tesseract "$output_tiff" "$output_txt" --psm 7 > /dev/null 2>&1
  done

python3 update.py
