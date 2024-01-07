from PIL import Image
import sys
if len(sys.argv) > 1:  # Checking if any argument is passed
    filename = sys.argv[1]  # The first argument after the script name
    print("Received filename:", filename)
    # Your function that utilizes the filename
else:
    print("No filename provided.")

screen = Image.open("../full_img/1.png")


x, y, w, h = 620, 310, 200, 50
screen.crop((x, y, x+w, y+h)).save("pot_size.png")
