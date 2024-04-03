import socket
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load model
model = tf.keras.models.load_model('model.h5')
print("Model loaded successfully.")

def preprocess_image(image_path, target_size=(86, 63)):
    image = load_img(image_path, target_size=target_size)
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def predict_image(image_path):
    preprocessed_image = preprocess_image(image_path)
    prediction = model.predict(preprocessed_image)
    return prediction[0][0]

# Setup socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen()

print("Listening for connections...")

player_status_file = "../player_status.txt"

while True:
    client_socket, addr = server_socket.accept()
    with client_socket:
        print(f"Connected by {addr}")
        image_path = client_socket.recv(1024).decode('utf-8')
        prediction = predict_image(image_path)
        number = image_path.split(".")[0]
        threshold = 0.5
        if prediction < threshold:
            result = f"{image_path} is a card"  
        else:
            result = f"{image_path} is not a card"
            with open(player_status_file, 'r') as file:
                    lines = file.readlines()
                
            for i, line in enumerate(lines):
                if line.startswith(f"{number}:"):
                    parts = line.split(':')
                    parts[1] = "folded\n"  # Update status to folded
                    lines[i] = ':'.join(parts)  
                    break                 

            with open(player_status_file, 'w') as file:
                file.writelines(lines)

            


        client_socket.sendall(result.encode('utf-8'))

