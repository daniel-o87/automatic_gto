#!/bin/bash

#rm *.png *.txt *.tiff
#FILENAME="$1"
sleep 3
echo "Starting to check stack"
python stack.py #"$FILENAME"
# Loop through each testing.png file in the directory
for file in *testing.png; do
    # Extract the base name without 'testing.png'
    base_name=$(echo "$file" | sed 's/testing.png//')

    # Define the output filenames for the TIFF and text files
    output_tiff="${base_name}.tiff"
    output_txt="${base_name}"

    convert "$file" -colorspace Gray -contrast-stretch 0% -threshold 50% "$output_tiff"

    # Run Tesseract OCR on the preprocessed TIFF file to extract text
    tesseract "$output_tiff" "$output_txt" --psm 7 > /dev/null 2>&1 

    # Check the OCR output
    #if [ -s "$output_txt" ]; then
        #echo "OCR result stored in $output_txt:"
        #cat "$output_txt"
    #else
        #echo "OCR failed to extract text from $output_tiff"
    #fi
    #head "$output_txt.txt"
done

#echo "Conversion and OCR processing completed."
./update_player_status.sh
