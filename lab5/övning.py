import cv2
import math
import random
'''
# Read the image
img = cv2.imread("C:/Users/felix/Skrivbord/python git/tdde23-2024-labbar-14-d1-b-05/lab5/plane.jpg")

# Check if the image was successfully loaded
if img is not None:
    print("Image shape:", img.shape)
    print("Image size:", img.size)

    # Remove the blue channel from the image
    img[:, :, 0] = 0  # Set the blue channel to 0 for all pixels

    # Display the modified image
    cv2.imshow('Modified Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found or unable to load.")
'''
'''
def create_lock(password, secret_message):
    def lock(input_password):
        if input_password == password:
            return secret_message
        else: 
            return "Wrong password"
    return lock

my_lock = create_lock(1234, "Secret message")
print(my_lock(42))
print(my_lock(1234))

double = lambda x: x*2
print(double(5))

sumsqr = lambda x, y: x**2 + y**2
print(sumsqr(3, 4))

adder = lambda x: lambda y: lambda z:x + y +z
print(adder(5))
print(adder(5)(3)(4))
'''
def stars(x, y):
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)

def skystar(img):
    if img is not None:
        # RBG
        height, width = img.shape[0], img.shape[1]
        # Loop over the image pixels
        for x in range(0, width):
            for y in range(0, height): 
                b, g, r = img[y, x]  # Get the pixel color
                if b > g+18 and b > r+18:
                    img[y, x] = stars(x, y)
        return img

img = cv2.imread("/home/fe1ixj/Desktop/python/tdde23-2024-labbar-14-d1-b-05/lab5/planec130.jpg")
if img is not None:
    new_img = skystar(img)
    cv2.imshow("filtered", new_img)  
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found or unable to load.")