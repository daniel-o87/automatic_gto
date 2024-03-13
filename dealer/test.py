from PIL import Image
import mss

players_loc = {"1": [206, 346, 75, 75] , "2": [565, 225, 75, 75],
               "3": [1261, 348, 75, 75], "4": [1200, 660, 75, 75],
               "5": [773, 706, 75, 75], "6": [314, 703, 50, 50], 
               "7": [240, 654, 75, 75]}

with mss.mss() as sct:
    # Loop through each player's location and capture it directly
    for player, coords in players_loc.items():
        # The screen part to capture
        monitor = {"top": coords[1], "left": coords[0], "width": coords[2], "height": coords[3]}
        sct_img = sct.grab(monitor)

        # Save the image file
        output_filename = f"{player}testing.png"
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output_filename)


# works
# 2,3,4, 5, 6, 7 
