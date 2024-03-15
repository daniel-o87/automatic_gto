from PIL import Image
import datetime
import sys
from mss import mss

timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
full_img_filename = f"../full_img/screenshot_{timestamp}.png"

with mss() as sct:
    sct.shot(output=full_img_filename)

players2 = {15: [533, 406, 86, 113],
             16: [622, 407, 86, 113],
             17: [710, 407, 86, 113],
            18: [801, 407, 86, 113], 
            19: [889, 407, 86, 113]}

"""x:533 y:406 screen:0 window:79691785
x:533 y:406 screen:0 window:79691785
x:533 y:406 screen:0 window:79691785
x:533 y:406 screen:0 window:79691785
x:626 y:407 screen:0 window:79691785
x:624 y:407 screen:0 window:79691785
x:624 y:407 screen:0 window:79691785
x:624 y:407 screen:0 window:79691785
x:624 y:407 screen:0 window:79691785
x:624 y:407 screen:0 window:79691785
x:709 y:414 screen:0 window:79691785
x:714 y:407 screen:0 window:79691785"""

players = {1: [145, 155, 63, 86],
            2: [685, 38, 63, 86],
            3: [1271, 155, 63, 86],
            4: [1287, 467, 63, 86],
            5: [925, 662, 63, 86],
            6: [445, 668, 63, 86],
            7: [112, 467, 63, 86],
            "flop": [533, 406, 86, 113],
           "turn": [801, 407, 86, 113], 
           "river": [889, 407, 86, 113]}

"""
players = {1: [145, 155, 63, 86],
            2: [208, 155, 63, 86],
            3: [685, 38, 63, 86],
            4: [748, 38, 63, 86],
            5: [1271, 155, 63, 86],
            6: [1334, 155, 63, 86],
            7: [1287, 467, 63, 86],
            8: [1350, 467, 63, 86],
            9: [925, 662, 63, 86],
            10: [988, 662, 63, 86],
            11: [445, 668, 63, 86],
            12: [508, 668, 63, 86],
            13: [112, 467, 63, 86],
            14: [177, 467, 63, 86], 
            15: [533, 406, 86, 113],
            16: [622, 407, 86, 113],
            17: [710, 407, 86, 113],
            18: [801, 407, 86, 113], 
            19: [889, 407, 86, 113]}
"""          
for i in players.keys():
    with Image.open(full_img_filename) as img:
        x, y, w, h = players[i][0], players[i][1], players[i][2], players[i][3]
        img.crop((x, y, x+w, y+h)).save(f"{i}.png")
