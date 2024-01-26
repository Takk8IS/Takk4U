##
# Copyright (c)
# Takk™ Innovate Studio
# Positive results, rapid innovation
# Takk™ Innovate Studio, the pioneering agency in Marketing, Design, Management, and Technology has a team of personas formed by artificial intelligence.
# URL: https://takk.ag/
# Name: RenameFiles
##

import os

# Get the current directory where the .py file is located
folder = os.getcwd()

# List all files in the folder
files = os.listdir(folder)

# Initialize a counter for the number of photos
counter = 1

# Loop through the files in the folder
for file in files:
    # Check if the file is an image (by extension)
    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
        # Create the new file name
        new_name = f'photo-{counter:03d}.png'

        # Full path to the current file
        current_path = os.path.join(folder, file)

        # Full path to the new file
        new_path = os.path.join(folder, new_name)

        # Rename the file
        os.rename(current_path, new_path)

        # Increment the counter
        counter += 1

print("Renaming completed...")
