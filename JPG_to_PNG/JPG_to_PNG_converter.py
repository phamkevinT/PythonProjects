import sys
import os
from PIL import Image

# Grab the first and second arguments from terminal
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# Check if output exists, if not create a folder for it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Go through each image in folder and convert to PNG
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    # remove the .jpg from the file name
    clean_name = os.path.splitext(filename)[0]
    # user will provide the '/' in their terminal argument
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('Image conversion completed!')
