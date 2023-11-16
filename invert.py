import os
from xml.etree import ElementTree as ET

# Define input and output directories
input_dir = './images'
output_dir = './white_images'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all files in input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.svg'):
        # Parse SVG file
        tree = ET.parse(os.path.join(input_dir, filename))
        root = tree.getroot()

        # Change fill color of all path elements to white
        for path in root.findall('.//{http://www.w3.org/2000/svg}path'):
            if 'fill' in path.attrib and path.attrib['fill'] == 'black':
                path.attrib['fill'] = 'white'

        # Save modified SVG to output directory
        tree.write(os.path.join(output_dir, filename))
