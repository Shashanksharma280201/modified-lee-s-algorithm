import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Function to handle mouse clicks
def click_event(event, x, y, flags, params):
    global points

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)  # Mark the point with a red circle
        points.append((x, y))
        cv2.imshow('Image', img)

# Create a Tkinter root window (hidden)
root = tk.Tk()
root.withdraw()

# Create a dictionary to store points for each label
pin_points = {}

# Ask the user for the number of input and output pins
num_inputs = int(input("Enter the number of input pins: "))

# Collect input pin labels and points
for i in range(1, num_inputs + 1):
    label = input(f"Enter a label for Input Pin {i}: ")
    pin_points[label] = []
    
    # Ask the user to select an image file
    file_path = filedialog.askopenfilename(title=f"Select an image file for {label}", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.tif")])

    if not file_path:
        print(f"No image selected for {label}. Exiting.")
        continue

    img = cv2.imread(file_path)

    if img is None:
        print(f"Could not open or read the image for {label}. Exiting.")
        continue

    points = []  # List to store the selected points

    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', click_event)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    pin_points[label] = points

# Ask the user for the number of output pins
num_outputs = int(input("Enter the number of output pins: "))

# Collect output pin labels and points
for i in range(1, num_outputs + 1):
    label = input(f"Enter a label for Output Pin {i}: ")
    pin_points[label] = []

    # Ask the user to select an image file
    file_path = filedialog.askopenfilename(title=f"Select an image file for {label}", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.tif")])

    if not file_path:
        print(f"No image selected for {label}. Exiting.")
        continue

    img = cv2.imread(file_path)

    if img is None:
        print(f"Could not open or read the image for {label}. Exiting.")
        continue

    points = []  # List to store the selected points

    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', click_event)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    pin_points[label] = points

# Ask the user to mark points for VDD
label = "VDD"
pin_points[label] = []

# Ask the user to select an image file for VDD
file_path = filedialog.askopenfilename(title=f"Select an image file for {label}", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.tif")])

if not file_path:
    print(f"No image selected for {label}. Exiting.")
else:
    img = cv2.imread(file_path)

    if img is None:
        print(f"Could not open or read the image for {label}. Exiting.")
    else:
        points = []  # List to store the selected points

        cv2.imshow('Image', img)
        cv2.setMouseCallback('Image', click_event)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        pin_points[label] = points

# Ask the user to mark points for GND
label = "GND"
pin_points[label] = []

# Ask the user to select an image file for GND
file_path = filedialog.askopenfilename(title=f"Select an image file for {label}", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.tif")])

if not file_path:
    print(f"No image selected for {label}. Exiting.")
else:
    img = cv2.imread(file_path)

    if img is None:
        print(f"Could not open or read the image for {label}. Exiting.")
    else:
        points = []  # List to store the selected points

        cv2.imshow('Image', img)
        cv2.setMouseCallback('Image', click_event)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        pin_points[label] = points

# Save the data to a text file
output_file = input("Enter the name of the output text file: ")
with open(output_file, 'w') as f:
    for label, points in pin_points.items():
        f.write(f"{label} (Image Dimensions: {img.shape[1]}x{img.shape[0]}):\n")
        for (x, y) in points:
            f.write(f"  ({x}, {y})\n")
        f.write("\n")

print(f"Data saved to {output_file}")
