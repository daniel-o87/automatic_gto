from PIL import Image
import sys
if len(sys.argv) > 1:  # Checking if any argument is passed
    filename = sys.argv[1]  # The first argument after the script name
    print("Received filename:", filename)
    # Your function that utilizes the filename
else:
    print("No filename provided.")

screenshot = Image.open("../full_img/1.png")


# NEED TO DO 7 FOR STACK SIZE
players_loc = {"1": [295, 565, 250, 55] , "2": [1100, 400, 250, 45],
               "3": [1975, 570, 250, 45], "4": [1990, 1025, 250, 65], 
               "5": [1465, 1320, 250, 45], "6": [745, 1320, 250, 45], 
               "7": [539, 940, 250, 45]}
for i in players_loc:
    crop = screenshot.crop((players_loc[i][0], players_loc[i][1], players_loc[i][0]+players_loc[i][2], players_loc[i][1]+players_loc[i][3]))
    crop.save(i+"testing.png")
