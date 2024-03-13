from PIL import Image
from mss import mss
import datetime
import os
import time



def take_screenshot_and_crop(coords):
    """Take a screenshot of the entire screen, save it, and crop the specified area."""
    # Generate a unique filename based on the current timestamp for the full screenshot
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    full_img_filename = f"../full_img/screenshot_{timestamp}.png"  # Saving in the ../full_img/ directory

    # Take a screenshot and save it
    with mss() as sct:
        sct.shot(output=full_img_filename)

    # Crop the screenshot and save it as rng.png
    with Image.open(full_img_filename) as img:
        cropped_img = img.crop((coords[0], coords[1], coords[0]+coords[2], coords[1]+coords[3]))
        cropped_img.save("rng.png")  # Saving cropped image in the current directory

    return full_img_filename

# Define the crop area: x, y, w, h
crop_area = [1371, 70, 28, 17] 

# Take a screenshot, crop it, and get the filename
screenshot_filename = take_screenshot_and_crop(crop_area)
print(screenshot_filename)
