#!/bin/bash

# Get the filename from the first argument
FILENAME="$1"

# Check if the filename is provided
if [ -z "$FILENAME" ]; then
    echo "No filename provided."
    exit 1
fi

# Your loop and other commands using $FILENAME
while true; do 
    echo "Doing stack_decision.sh with $FILENAME"
    cd ../stack_decision && ./bash.sh #"$FILENAME"
    #cd ../pot && ./bash.sh "$FILENAME"
    #cd ../turn_to_move && ./bash.sh "$FILENAME"
    #cd ../bet_size && ./bash.sh "$FILENAME"
    echo "True"
    #sleep 2  # Optional delay
done
