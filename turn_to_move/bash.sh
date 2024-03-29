#!/bin/bash

rm *.png *.tiff *.txt
FILENAME="$1"
echo "turn_to_move"
python ready.py "$FILENAME"

# Loop through each .tiff file in the directory
for file in *_enhanced.tiff; do
    # Extract the base name without '_enhanced.tiff'
    base_name=$(echo "$file" | sed 's/_enhanced.tiff//')

    # Define the output text file name
    output_txt="${base_name}"

    # Run Tesseract OCR on the .tiff file to extract text
    # Note: Change 'eng' to your desired language code if necessary
    tesseract "$file" "$output_txt" --psm 7 > /dev/null 2>&1

    # Optional: Output the OCR results to the console
    #echo "OCR results for $file stored in $output_txt:"
    #cat "$output_txt"
done

#echo "Tesseract OCR processing completed for all images."

