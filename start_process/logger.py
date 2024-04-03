from datetime import datetime
import os

with open("game.txt", 'w') as file:
    pass

dt_string = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.txt'

os.makedirs("../game_logs", exist_ok=True)

old_name = "game.txt"
new_name = f"../game_logs/{dt_string}"

os.rename(old_name, new_name)

with open("../game.txt", 'w') as file:
    pass  
print("Starting new hand")
