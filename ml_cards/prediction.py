import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np


def preprocess_image(image_path, target_size=(86, 63)):
    # Load the image file
    image = load_img(image_path, target_size=target_size)  
    # Convert the image to a numpy array
    image = img_to_array(image)
    # Scale the image pixels to the range [0, 1]
    image = image / 255.0

    # Add a batch dimension
    image = np.expand_dims(image, axis=0)
    return image

"""image = load_img('non_card.png', target_size=(86, 63))  
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

prediction = model.predict(image)
"""

model = tf.keras.models.load_model('model.h5')
print("Model loaded successfully.")

# Define the threshold
threshold = 0.5
for i in range(1, 20):
    image_path = f"{i}.png"
    preprocessed_image = preprocess_image(image_path)

    # Predict
    prediction = model.predict(preprocessed_image)

# Interpret the prediction based on the threshold
    print(f"Checking {i}.png", end = " ")
    print(f" Prediction result is {prediction[0][0]}")
    if prediction[0][0] < threshold:
        print(f"Image is a card.")
    else:
        print(f"Image is no_card.")



"""for i in range(1, 20):
        image = load_img(f'{i}.png', target_size=(86, 63))  
            image = img_to_array(image)
                image = np.expand_dims(image, axis=0)

                    prediction = model.predict(image)

                        # Interpret the prediction based on the threshold
                            if prediction[0][0] > threshold:
                                        print(f"Image {i} is a card.")
                                            else:
                                                        print(f"Image {i} is no_card.")
                                                        """
