import os
from PIL import Image

# Define the input directory containing the images
input_dir = '/home/adian/Work/PLUS/i3/project/Datasets/Massachusetts_Roads/tiff_1500/labels'

# Create the output directory if it doesn't already exist
output_dir = '/home/adian/Work/PLUS/i3/project/Datasets/Massachusetts_Roads/png_1500/labels'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Loop through each image in the input directory
for i, filename in enumerate(os.listdir(input_dir)):

    # Load the image
    image = Image.open(os.path.join(input_dir, filename))

    # Resize the image
    #image = image.resize((512, 512))

    # Save the image as png
    filename = f'{os.path.splitext(filename)[0]}.png'
    image.save(os.path.join(output_dir, filename))
    print(filename + " successfully resized and saved")
