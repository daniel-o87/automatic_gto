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

def process_images_for_active_players(filename, players_loc, active_players):
    """Processes images only for active players."""
    screenshot = Image.open("../full_img/" + filename)
    for player in players_loc:
        if player in active_players:
            coords = players_loc[player]
            crop = screenshot.crop((coords[0], coords[1], coords[0]+coords[2], coords[1]+coords[3]))
            crop.save(player + "testing.png")

# Check if a filename is provided
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("No filename provided.")
    sys.exit(1)

# Read player status
player_status_file = '../player_status.txt'  # Update with the correct path
active_players = read_player_status(player_status_file)

# Dictionary of coordinates with unique keys
players_loc = {"1": [545, 590, 50, 50], "2": [1350, 425, 50, 40], 
               "3": [2215, 595, 50, 40], "4": [2242, 1054, 50, 50],  
               "5": [1707, 1345, 50, 50], "6": [992, 1345, 50, 50], 
               "7": [500, 1054, 50, 50]}

# Process images for active players
process_images_for_active_players(filename, players_loc, active_players)
