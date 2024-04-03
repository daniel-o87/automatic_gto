#!/bin/bash

i3-msg workspace 6
while true; do
    echo "start_process"

    # Run the Python script and capture the output filename
    FILENAME=$(python check_rng.py)

    # Convert the cropped image to TIFF format
	convert rng.png -contrast-stretch 0% -colorspace Gray -density 300 aaaaa.tiff

        # Run Tesseract OCR on the preprocessed TIFF file to extract text
    tesseract aaaaa.tiff eng --psm 7 > /dev/null 2>&1

    # Read the content of eng.txt
	first_three=$(head -n 1 eng.txt | cut -c 1-3)

    # Check the content
    if [ "$first_three" == "RNG" ]; then
	python logger.py
#	cd ../pot && ./test.sh
        # Write player status to player_status.txt
        #cd ../
	#cd ../pot && ./bash.sh
	echo "RNG IS MET"
	sleep 1
	cd ../dealer && ./bash.sh
#	cd ../stack_decision && ./bash.sh
	break
    fi
done
