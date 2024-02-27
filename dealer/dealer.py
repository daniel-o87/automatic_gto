
from PIL import Image
import sys
def read_player_status(file_path):
    active_players = set()
    with open(file_path, 'r') as file:
        for line in file:
            player, status = line.strip().split(':')
            if status == 'active':
                active_players.add(player)
    return active_players

def process_images_for_active_players(filename, players_loc, active_players):
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


players_loc = {"1": [206, 346, 75, 75] , "2": [565, 225, 75, 75],
               "3": [1261, 348, 75, 75], "4": [1200, 660, 75, 75],
               "5": [773, 706, 75, 75], "6": [314, 703, 50, 50], 
               "7": [240, 654, 75, 75]}

process_images_for_active_players(filename, players_loc, active_players)
