import sys

def remove(number):
    lines = []  
    with open("player_status.txt", 'r') as file:
        lines = file.readlines()

    status = {}  

    for line in lines:
        parts = line.strip().split(':')  
        if len(parts) == 2: 
            player_number, player_status = parts
            try:
                player_number = int(player_number)
                if player_number == number:
                    status[player_number] = "folded"
                else:
                    status[player_number] = player_status              
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")

    with open("player_status.txt", "w") as file:
        for player in status:
            file.write(f"{player}:{status[player]}\n")

if __name__=="__main__":
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        remove(num)
    else:
        print("Wrong usage bro")
