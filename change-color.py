
import os
import xml.etree.ElementTree as ET

# Define the color you want to use
color = "#00BFFF" # DodgerBlue
# color = "#F7DF1E" # Yellow

# Loop through all SVG files in the images directory
for filename in os.listdir("images"):
    if filename.endswith(".svg"):
        # Parse the SVG file
        tree = ET.parse(os.path.join("images", filename))
        root = tree.getroot()

        # Find all path tags and change their fill property to the desired color
        for path in root.findall(".//{http://www.w3.org/2000/svg}path"):
            path.set("fill", color)

        # Save the modified SVG file
        tree.write(os.path.join("images", filename))
