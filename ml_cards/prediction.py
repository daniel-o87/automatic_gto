import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

model = tf.keras.models.load_model('model.h5')
print("Model loaded successfully.")

# Define the threshold
threshold = 0.5

image = load_img('3.png', target_size=(86, 63))  
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

prediction = model.predict(image)

# Interpret the prediction based on the threshold
print(prediction[0][0])
if prediction[0][0] > threshold:
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
