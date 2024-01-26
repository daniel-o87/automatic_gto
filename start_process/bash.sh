#!/bin/bash

while true; do
    echo "start_process"

    # Run the Python script and capture the output filename
    FILENAME=$(python check_rng.py)

    # Convert the cropped image to TIFF format
    convert rng.png output.tiff

    # Run Tesseract OCR on the TIFF image
    tesseract --psm 7 output.tiff eng > /dev/null 2>&1

    # Read the content of eng.txt
    file_content=$(cat eng.txt)

    # Check the content
    if [ "$file_content" == "RNG in progress" ]; then
        # Write player status to player_status.txt
        cd ../
        cat > player_status.txt <<EOF
1:active
2:active
3:active
4:active
5:active
6:active
7:active
EOF
        cd -  # Return to the start_process directory
        echo "YAY"
        echo "Doing call_bashes.sh with $FILENAME"
        ./call_bashes.sh "$FILENAME"

        # Empty eng.txt to reset the condition
        > eng.txt

        # Optional: Add a delay before the next loop iteration
        sleep 2
    else
        echo "RNG check in progress..."
    fi

    # Delay to prevent high CPU usage, adjust as needed
    sleep 0.5
done
