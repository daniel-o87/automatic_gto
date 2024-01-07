from PIL import Image
import sys
if len(sys.argv) > 1:  # Checking if any argument is passed
    filename = sys.argv[1]  # The first argument after the script name
    print("Received filename:", filename)
    # Your function that utilizes the filename
else:
    print("No filename provided.")

screenshot = Image.open("../full_img/1.png")

players_loc = {"1": [575, 625, 250, 50] , "2": [1070, 550, 250, 50 ],
               "3": [1610, 630, 250, 40], "4": [1610, 935, 250, 50], 
               "5": [1425, 1090, 250, 50], "6": [710, 1090, 250, 40], 
               "7": [539, 940, 250, 40]}

for i in players_loc:
    crop = screenshot.crop((players_loc[i][0], players_loc[i][1], players_loc[i][0]+players_loc[i][2], players_loc[i][1]+players_loc[i][3]))
    crop.save(i+"testing.png")
