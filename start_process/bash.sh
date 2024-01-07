#!/bin/bash


#if find . -name "*.tifff" > /dev/null; then
#  rm *.txt *.tiff *.png
#fi

FILENAME="$1"
echo "start_process"
python check_rng.py "$FILENAME"

convert rng.png output.tiff

tesseract output.tiff eng --oem 2 --psm 7 > /dev/null 2>&1
if grep -q "RNG in progress" eng.txt; then
  cd ../pot && ./bash.sh "$FILENAME"
  cd ../stack_decision && ./bash.sh "$FILENAME"
  cd ../turn_to_move && ./bash.sh "$FILENAME"
  cd ../bet_size && ./bash.sh "$FILENAME"
  echo "True"
else
  echo "False"
fi
