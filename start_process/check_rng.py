"""#1950 215
from PIL import Image
filename = ""

import sys
if len(sys.argv) > 1:  # Checking if any argument is passed
    filename = sys.argv[1]  # The first argument after the script name
    print("Received filename:", filename)
    # Your function that utilizes the filename
else:
    print("No filename provided.")

screen = Image.open("../full_img/"+filename)
x, y, w, h = 2000, 250, 250, 75

screen.crop((x, y, w+x, h+y)).save("rng.png")

from PIL import Image
from mss import mss
import datetime

def take_screenshot_and_crop(crop_area):
    # Generate a unique filename based on the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"../full_img/screenshot_{timestamp}.png"

    # Take a screenshot and save it
    with mss() as sct:
        sct.shot(output=filename)

    # Crop the screenshot
    with Image.open(filename) as img:
        cropped_img = img.crop(crop_area)
        cropped_img.save("rng.png")

    return filename

# Define the crop area: x, y, w, h
crop_area = (2000, 250, 250, 75)  # (x, y, x+w, y+h)

# Take a screenshot, crop it, and get the filename
screenshot_filename = take_screenshot_and_crop(crop_area)
print(screenshot_filename)


"""
from PIL import Image
from mss import mss
import datetime
import os

def take_screenshot_and_crop(crop_area):
    """Take a screenshot of the entire screen, save it, and crop the specified area."""
    # Generate a unique filename based on the current timestamp for the full screenshot
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    full_img_filename = f"../full_img/screenshot_{timestamp}.png"  # Saving in the ../full_img/ directory

    # Take a screenshot and save it
    with mss() as sct:
        sct.shot(output=full_img_filename)

    # Crop the screenshot and save it as rng.png
    with Image.open(full_img_filename) as img:
        cropped_img = img.crop(crop_area)
        cropped_img.save("rng.png")  # Saving cropped image in the current directory

    return full_img_filename

# Define the crop area: x, y, w, h
crop_area = (2000, 250, 2250, 325)  # (x, y, x+w, y+h)

# Take a screenshot, crop it, and get the filename
screenshot_filename = take_screenshot_and_crop(crop_area)
print(screenshot_filename)
