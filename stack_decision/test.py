import os
import re

def update_player_status(txt_directory, player_status_file):
    # Loop through each .txt file in the directory
    for file in os.listdir(txt_directory):
        if file.endswith(".txt"):
            player = os.path.splitext(file)[0]
            file_path = os.path.join(txt_directory, file)

            # Check if the file contains the word "Fold"
            with open(file_path, 'r') as f:
                content = f.read()
                if "ee" in content:
                    print("HE FOLDS HE FOLDS")
                    # Update player status to 'folded' in player_status.txt
                    with open(player_status_file, 'r+') as status_file:
                        status_content = status_file.read()
                        status_file.seek(0)
                        status_file.truncate()
                        updated_content = re.sub(rf'^{player}:.*', f'{player}:folded', status_content, flags=re.MULTILINE)
                        status_file.write(updated_content)

txt_directory = "./"  # Adjust if needed
player_status_file = "../player_status.txt"  # Path to player_status.txt
update_player_status(txt_directory, player_status_file)
print("Player status updated.")

