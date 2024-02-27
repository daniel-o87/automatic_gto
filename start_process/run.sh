#!/bin/bash



sleep 4 
python check_rng.py
convert rng.png -colorspace Gray -density 300 -threshold 50% aaaaa.tiff
tesseract aaaaa.tiff eng 
