import cv2
import random
import numpy
from cvlib import *
from lab5a import cvimg_to_list


#Lab5b1
def pixel_constraint(h_low, h_high, s_low, s_high, v_low, v_high):
    '''Returns a function that takes a pixel and returns 1 if the pixel is within the HSV range, 0 otherwise.'''
    def constraint(pixel):
        if len(pixel) == 3:
            if all(isinstance(i, int) for i in pixel):
                for i in pixel:
                    if i < 0 or i > 255:
                        raise ValueError("Pixel values must be in range 0-255")
                (h, s, v) = pixel  # Hue, saturation, value
                if h >= h_low and h <= h_high and s >= s_low and s <= s_high and v >= v_low and v <= v_high:
                    return 1
                else:
                    return 0
            else:
                raise TypeError("Pixel must be a tuple of integers")
        else: 
            raise ValueError("Pixel must be a tuple of length 3")
    return constraint


#Lab5b2 
def generator_from_image(img_list):
    '''Returns a function that takes an index and returns the color of the pixel at that index.'''
    if not isinstance(img_list, list) or len(img_list)==0: 
        raise ValueError("Input must be a list and not empty") 
    def get_pixel_color(index):
        if index > len(img_list):
            raise IndexError("Index out of range")
        else:
            if len(img_list[index]) == 3:
                return img_list[index]
    return get_pixel_color


#Lab5b3
def combine_images(hsv, condition, generator1, generator2):
    '''Returns a list of pixels that is a combination of two images'''
    try:
        generator1_list = [generator1(i) for i in range(len(hsv))]
        generator2_list = [generator2(i) for i in range(len(hsv))]

        return [add_tuples(multiply_tuple(generator1_list[i], condition(hsv[i])),
                multiply_tuple(generator2_list[i], (1 - condition(hsv[i])))) for i in range(len(hsv))]
    except IndexError:
        raise IndexError("Index out of range")
    except ValueError:
        raise ValueError("Input must be a list and not empty")
    except TypeError:
        raise TypeError("Input must be a list and not empty")   
        

# Skapa en generator som gör en stjärnhimmel
def generator1(index):
    '''Returns a random patern of stars in the sky.'''
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)


#Lab5b4
def gradient_condition(pixel): 
    '''Returns a value between 0 and 1 for different shades of gray.''' 
    return round(pixel[0] / 255, 2)


#Testcode
def test_lab5b1():
    '''Test lab5b1.'''
    hsv_plane = cv2.cvtColor(cv2.imread("/home/fe1ixj/Desktop/python/tdde23-2024-labbar-14-d1-b-05/lab5/planec130.jpg"), cv2.COLOR_BGR2HSV)
    plane_list = cvimg_to_list(hsv_plane)
    is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
    sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list))) # Multiply by 255 to get a visible color
    
    cv2.imshow('sky', greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
    cv2.waitKey(0)


def test_lab5b2():
    '''Test lab5b2.'''
    orig_img = cv2.imread("/home/fe1ixj/Desktop/python/tdde23-2024-labbar-14-d1-b-05/lab5/planec130.jpg")
    orig_list = cvimg_to_list(orig_img)
    generator = generator_from_image(orig_list)
    new_list = [generator(i) for i in range(len(orig_list))]

    cv2.imshow('original', orig_img)
    cv2.imshow('new', rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))
    cv2.waitKey(0)


def test_lab5b3():
    '''Test lab5b3.'''
    # Läs in en bild
    plane_img = cv2.imread("/home/fe1ixj/Desktop/python/tdde23-2024-labbar-14-d1-b-05/lab5/planec130.jpg")
    # Skapa ett filter som identifierar himlen
    condition = pixel_constraint(100, 150, 50, 200, 100, 255)
    # Omvandla originalbilden till en lista med HSV-färger
    hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
    plane_img_list = cvimg_to_list(plane_img)
    # Skapa en generator för den inlästa bilden
    generator2 = generator_from_image(plane_img_list)
    # Kombinera de två bilderna till en, alltså använd himmelsfiltret som mask
    result = combine_images(hsv_list, condition, generator1, generator2)
    # Omvandla resultatet till en riktig bild och visa upp den
    new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])

    cv2.imshow('Final image', new_img)
    cv2.imshow('Original', plane_img)
    cv2.waitKey(0)

def test_lab5b4():
    '''Test lab5b4.'''
    flower_img = cv2.imread("/home/fe1ixj/Desktop/python/tdde23-2024-labbar-14-d1-b-05/lab5/flowers.jpg")
    gradient_img = cv2.imread("/home/fe1ixj/Desktop/python/tdde23-2024-labbar-14-d1-b-05/lab5/gradient.jpg")
    plane_img = cv2.imread("/home/fe1ixj/Desktop/python/tdde23-2024-labbar-14-d1-b-05/lab5/planec130.jpg")
    flower_img_list = cvimg_to_list(flower_img)
    gradient_img_list = cvimg_to_list(gradient_img)
    plane_img_list = cvimg_to_list(plane_img)


    generator3 = generator_from_image(flower_img_list)
    generator4 = generator_from_image(plane_img_list)

    res = combine_images(gradient_img_list, gradient_condition, generator3, generator4)
    new_img = rgblist_to_cvimg(res, gradient_img.shape[0], gradient_img.shape[1])

    cv2.imshow('Final image2', new_img)
    cv2.waitKey(0)

if __name__ == '__main__':
    test_lab5b1()
    test_lab5b2()
    test_lab5b3()
    test_lab5b4()