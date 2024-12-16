import cv2
import numpy as np

def invert_colors(img):
    # Invert the colors of the image
    inverted_img = 255 - img

    return inverted_img

# Example usage
img = cv2.imread("/home/fe1ixj/Desktop/python/tdde23-2024-labbar-14-d1-b-05/lab5/plane.jpg")

if img is not None:
    inverted_img = invert_colors(img)
    cv2.imwrite("inverted_image.jpg", inverted_img)
else:
    print("Error: Image not found or unable to load.")


