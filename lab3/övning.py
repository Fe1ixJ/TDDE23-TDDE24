import cv2

img = cv2.imread('plane.jpg')     # Läs in en bild från en fil
img[0,0]                          # Visa värdet av pixeln i ena hörnet
print(img[0,0])                   # Skriv ut värdet av pixeln lite mer läsbart
img[0,0][2] = 0                   # Förändra värdet av r-komponenten 