#1950 215
from PIL import Image

import sys
if len(sys.argv) > 1:  # Checking if any argument is passed
    filename = sys.argv[1]  # The first argument after the script name
    print("Received filename:", filename)
    # Your function that utilizes the filename
else:
    print("No filename provided.")

screen = Image.open("../full_img/14.png")
x, y, w, h = 2000, 250, 250, 75

screen.crop((x, y, w+x, h+y)).save("rng.png")
