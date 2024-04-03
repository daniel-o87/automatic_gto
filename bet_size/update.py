import os

# Like the name says
def contains_no_letters(s):
        return not any(char.isalpha() for char in s)
# adds the decimal value from 2 spaces from the back
def modification(s):
    output = ""
    if not "." in s:
        beg = s[1:-2]
        end = s[-2:]
        output = "".join(beg) + "." + "".join(end)
    else:
        beg = s[1:-2]
        end = s[-2:]
        output = "".join(beg) + "".join(end)
    return output

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
                content = file.readlines()
                print(f"file {file_name} before mods {content}")
                a = modification(content)
            with open(file_path, 'w') as file:
                file.writelines(a)
# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Update with the correct path for player_status.txt
player_status_file = '../player_status.txt'  
active_players = read_player_status(player_status_file)
print("Active players:", active_players)

# Read .txt files for active players
read_txt_files(current_directory, active_players)
