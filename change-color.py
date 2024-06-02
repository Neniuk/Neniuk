import os
import xml.etree.ElementTree as ET

# Icons from: https://devicon.dev/

# Define the color you want to use
color = "#00BFFF"  # DodgerBlue
# color = "#F7DF1E" # Yellow

# Loop through all SVG files in the icons directory
for filename in os.listdir("icons"):
    if filename.endswith(".svg"):
        try:
            # Parse the SVG file
            tree = ET.parse(os.path.join("icons", filename))
            root = tree.getroot()

            # Find all path tags and change their fill property to the desired color
            for path in root.findall(".//{http://www.w3.org/2000/svg}path"):
                path.set("fill", color)

            # Save the modified SVG file
            tree.write(os.path.join("icons", filename))
        except ET.ParseError as e:
            print(f"Error parsing file: {filename}")
            print(e)
