import cv2
import sys
if len(sys.argv) > 1:  # Checking if any argument is passed
    filename = sys.argv[1]  # The first argument after the script name
    print("Received filename:", filename)
    # Your function that utilizes the filename
else:
    print("No filename provided.")

# Load image
image = cv2.imread('../full_img/' + filename)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Increase contrast here if needed

# Apply thresholding to isolate white text
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Dilate/Erode to reduce noise and close gaps in text
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Resize image to increase DPI for Tesseract
desired_dpi = 300.0
height, width = thresh.shape
scale_factor = desired_dpi / 72  # Assume original DPI is 72
new_height, new_width = int(height * scale_factor), int(width * scale_factor)
resized_img = cv2.resize(thresh, (new_width, new_height))

# Save the result as TIFF
cv2.imwrite('enhanced_result.tiff', resized_img)

# Now run Tesseract on the enhanced_result.tiff

