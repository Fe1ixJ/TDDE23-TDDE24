import cv2
import numpy
import math


def cvimg_to_list(img):
    """Return a list of pixels from an OpenCV image."""
    height, width = img.shape[0], img.shape[1]
    # A list that will contain the image data
    lst = []
    # Loop over the image pixels
    for y in range(0, height):
        for x in range(0, width): 
            b, g, r = img[y, x]  # Get the pixel color (fixed indexing)
            lst.append([int(b), int(g), int(r)])  # Convert to regular int for readability
    return lst


def unsharp_mask(N):
    """The function takes an integer N and returns a 2D list representing a Gaussian blur kernel."""
    S = 4.5
    return [[(-1/(2*math.pi*S**2))*math.exp(-1/2*(x**2 + y**2)/S**2) if (x, y) != (0, 0) 
            else 1.5 for x in range(-N//2+1, N//2+1)] for y in range(-N//2+1, N//2+1)]


# Test code
def test_lab5a():
    '''Test lab5a.'''
    img = cv2.imread("/home/fe1ixj/Desktop/python/tdde23-2024-labbar-14-d1-b-05/lab5/gustaf.jpg") 

    print(cvimg_to_list(img)[:10])
    #print(unsharp_mask(3))
    # Apply the unsharp mask
    kernel = numpy.array(unsharp_mask(11))
    sharpen_img = cv2.filter2D(img, -1, kernel)

    # Display the sharpened and original images
    cv2.imshow("filtered", sharpen_img)
    cv2.imshow("original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    '''
# How I would do it without list builders 
def unsharp_mask2(N):
    S = 4.5
    Neg_Gaussisk_blur = [[(-1/(2*math.pi*S**2))*math.e**(-1/2*(x**2 + y**2)/S**2)]] # Gaussian blur calculation
    if (x,y) != (0,0): # If the pixel is not the center pixel
        return 1.5
    for x in range(-N//2+1, N//2+1): # Loop over the kernel. 
        for y in range(-N//2+1, N//2+1): 
            return Neg_Gaussisk_blur
''' 
if __name__ == '__main__':
    test_lab5a()