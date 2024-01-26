#!/bin/bash

# Directory where .txt files are located
txt_directory="./"  # Adjust if needed
player_status_file="../player_status.txt"  # Path to player_status.txt

# Loop through each .txt file in the directory
for file in "$txt_directory"*.txt; do
    # Extract the player number from the filename
    player=$(basename "$file" ".txt")

    # Check if the file contains the word "Fold"
    if grep -qi "Fold" "$file"; then
        echo "HE FOLDS HE FOLDS"
        # Update player status to 'folded' in player_status.txt
        sed -i '' "s/^$player:.*/$player:folded/" "$player_status_file"
    fi
done

echo "Player status updated."

