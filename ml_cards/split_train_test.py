import os
import shutil
import random

def split_data(source_folder, train_folder, test_folder, split_ratio=0.75):
    # Ensure randomness
    random.seed(42)

    for category in ["cards", "no_cards"]:
        # Build paths for source, train, and test folders for the current category
        source_path = os.path.join(source_folder, category)
        train_path = os.path.join(train_folder, category)
        test_path = os.path.join(test_folder, category)

        # Create train and test category folders if they don't exist
        os.makedirs(train_path, exist_ok=True)
        os.makedirs(test_path, exist_ok=True)

        # List all files in the current source category folder
        files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]
        # Shuffle files to ensure random splitting
        random.shuffle(files)

        # Split files according to the specified ratio
        split_index = int(len(files) * split_ratio)
        train_files = files[:split_index]
        test_files = files[split_index:]

        # Move files to the respective train and test folders
        for f in train_files:
            shutil.move(os.path.join(source_path, f), train_path)

        for f in test_files:
            shutil.move(os.path.join(source_path, f), test_path)

# Define source, train, and test folders
source_folder = '/home/do/Desktop/fun_testing/ml_cards/holder'
train_folder = '/home/do/Desktop/fun_testing/ml_cards/train'
test_folder = '/home/do/Desktop/fun_testing/ml_cards/test'

# Perform the split
split_data(source_folder, train_folder, test_folder, split_ratio=0.75)

print("Data split and moved successfully.")

