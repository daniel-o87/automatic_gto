import cv2
import numpy as np
import pytesseract

# Set the path to the Tesseract command if it's not in your PATH
# Uncomment and update the path below only if necessary
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Path to your image
for i in range(1, 8):
    image_path = f"/home/do/Desktop/fun_testing/automatic_gto/stack_decision/{i}testing.png"
    # Load the image with OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use adaptive thresholding to handle different lighting conditions
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY, 11, 2)

    # Optionally, apply dilation to make the text more prominent
    kernel = np.ones((1, 1), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=1)

    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(dilated)

    # Print the extracted text
    print(text)
