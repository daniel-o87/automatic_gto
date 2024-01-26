import os
from PIL import Image
import sys

def read_player_status(file_path):
    """Reads the player status from the file and returns a set of active players."""
    active_players = set()
    with open(file_path, 'r') as file:
        for line in file:
            player, status = line.strip().split(':')
            if status == 'active':
                active_players.add(player)
    return active_players

def read_txt_files(directory, file_prefixes):
    """Reads .txt files starting with specific prefixes in the given directory."""
    for prefix in file_prefixes:
        file_name = f"{prefix}.txt"
        file_path = os.path.join(directory, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                # Process the file as needed
                print(f"Contents of {file_name}:")
                print(file.read())

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Update with the correct path for player_status.txt
player_status_file = '../player_status.txt'  
active_players = read_player_status(player_status_file)
print("Active players:", active_players)

# Read .txt files for active players
read_txt_files(current_directory, active_players)
