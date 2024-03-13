from PIL import Image
import datetime
import sys
from mss import mss

timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
full_img_filename = f"../full_img/screenshot_{timestamp}.png"

with mss() as sct:
    sct.shot(output=full_img_filename)

with Image.open(full_img_filename) as img:
    x, y, w, h = 345, 96, 190, 29
    img.crop((x, y, x+w, y+h)).save("image.png")
