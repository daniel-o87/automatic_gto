import os
from PIL import Image
import subprocess
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
                content = file.read().strip()  # Read and strip the file content
                if "D" in content:  # Check if "D" is in the content
                    print(f"Player {prefix} is the dealer:")
                    # Construct the path to order.py
                    order_py_path = os.path.join(directory, '..', 'order.py')
                    # The correct path to player_status.txt based on your setup
                    player_status_path = os.path.join(directory, '..', 'player_status.txt')
                    # Call order.py with the path to player_status.txt and the dealer's prefix
                    subprocess.run(['python3', order_py_path, player_status_path, prefix], check=True)

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Update with the correct path for player_status.txt
player_status_file = '../player_status.txt'  
active_players = read_player_status(player_status_file)
print("Active players:", active_players)

# Read .txt files for active players
read_txt_files(current_directory, active_players)

