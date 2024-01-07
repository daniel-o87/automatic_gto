from PIL import Image
import cv2
import sys
if len(sys.argv) > 1:  # Checking if any argument is passed
    filename = sys.argv[1]  # The first argument after the script name
    print("Received filename:", filename)
        # Your function that utilizes the filename
else:
    print("No filename provided.")

# Dictionary of coordinates with unique keys
players_loc = {"1": [545, 590, 50, 50], "2": [1350, 425, 50, 40], 
               "3": [2215, 595, 50, 40], "4": [2242, 1054, 50, 50],  
               "5": [1707, 1345, 50, 50], "6": [992, 1345, 50, 50], 
               "7": [500, 1054, 50, 50]}

# Open the main image
screen = Image.open("../full_img/10.png")

# Loop through the coordinates, crop, and save images
for key, (x, y, w, h) in players_loc.items():
    cropped = screen.crop((x, y, x + w, y + h))
    cropped.save(f"{key}.png")
    
    # Read the saved image
    image = cv2.imread(f"{key}.png")
    
    # Convert to grayscale and apply thresholding to isolate white text
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    
    # Dilate/Erode to reduce noise and close gaps in text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    # Resize image to increase DPI for Tesseract
    height, width = thresh.shape
    scale_factor = 300.0 / 72  # Convert to desired DPI
    new_height, new_width = int(height * scale_factor), int(width * scale_factor)
    resized_img = cv2.resize(thresh, (new_width, new_height))
    
    # Save the result as TIFF
    cv2.imwrite(f'{key}_enhanced.tiff', resized_img)
