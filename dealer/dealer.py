
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


players_loc = {"1": [360, 641, 100, 100] , "2": [900, 480, 100, 100],
               "3": [1920, 650, 100, 100], "4": [1850, 1140, 50, 50],
               "5": [1200, 1180, 100, 100], "6": [510, 1185, 100, 100], 
               "7": [395, 1100, 100, 100]}

process_images_for_active_players(filename, players_loc, active_players)
