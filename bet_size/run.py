from PIL import Image
import mss

players_loc = {
    "1": [379, 322, 150, 30], "2": [691, 269, 150, 30],
    "3": [1060, 322, 150, 30], "4": [1068, 531, 150, 30],
    "5": [939, 638, 150, 30], "6": [452, 634, 150, 30],
    "7": [362, 532, 150, 30]
}

with mss.mss() as sct:
    # Loop through each player's location and capture it directly
    for player, coords in players_loc.items():
        # The screen part to capture
        monitor = {"top": coords[1], "left": coords[0], "width": coords[2], "height": coords[3]}
        sct_img = sct.grab(monitor)

        # Save the image file
        output_filename = f"{player}_testing.png"
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output_filename)
        print(f"Saved {output_filename}")


# works
#3, 4, 5 6, 7
