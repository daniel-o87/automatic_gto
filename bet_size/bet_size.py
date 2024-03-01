from PIL import Image
from mss import mss
import datetime
import os
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

def take_screenshot_and_crop(players_loc, active_players):
    """Take a screenshot of the entire screen and crop for each active player."""
    # Generate a unique filename based on the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    full_img_filename = f"../full_img/screenshot_{timestamp}.png"

    # Take a screenshot and save it
    with mss() as sct:
        sct.shot(output=full_img_filename)

    # Crop the screenshot for each active player
    for player in players_loc:
        if player in active_players:
            coords = players_loc[player]
            with Image.open(full_img_filename) as img:
                cropped_img = img.crop((coords[0], coords[1], coords[0]+coords[2], coords[1]+coords[3]))
                cropped_img.save(player + "testing.png")

# Player locations (example for bet_size folder, adjust for others)
players_loc = {
    "1": [379, 322, 150, 30], "2": [691, 269, 150, 30],
    "3": [1060, 322, 150, 30], "4": [1068, 531, 150, 30],
    "5": [939, 638, 150, 30], "6": [452, 634, 150, 30],
    "7": [362, 532, 150, 30]
}

# Read player status
player_status_file = '/home/do/Desktop/fun_testing/automatic_gto/player_status.txt'

# Continuously take screenshots and process
active_players = read_player_status(player_status_file)
take_screenshot_and_crop(players_loc, active_players)

