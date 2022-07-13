from locale import atoi
from sys import argv
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sys import argv

def absoluteSobel(sobelXY):
    return np.uint8(np.absolute(sobelXY))

def SobelGradient(gray_img, ABS_FLAG):
    sobelX = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0)
    sobelY = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1)
    if ABS_FLAG == 1:
        sobelX = absoluteSobel(sobelX)
        sobelY = absoluteSobel(sobelY)
    plt.subplot(1, 3, 1), plt.imshow(gray_img), plt.axis("off"), plt.title("gray_img")
    plt.subplot(1, 3, 2), plt.imshow(sobelX), plt.axis("off"), plt.title("sobelX")
    plt.subplot(1, 3, 3), plt.imshow(sobelY), plt.axis("off"), plt.title("sobelY")
    plt.show()
    sobelCombined = cv2.bitwise_or(sobelX, sobelY)
    plt.imshow(sobelCombined), plt.axis("off"), plt.title("sobel")
    plt.show()
    
    
if __name__ == "__main__":
    gray_img = cv2.imread('gray_homework.png')
    print("gray_img shape: ", gray_img.shape)
    print("gray_img type: ", type(gray_img))
    try:
        ABS_FLAG = atoi(argv[1])
    except:
        ABS_FLAG = 1
    SobelGradient(gray_img, ABS_FLAG) 