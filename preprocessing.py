#Reference: https://code.tutsplus.com/tutorials/image-filtering-in-python--cms-29202

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Median filter
def preprocess(image, median_size=5):
    # It supports maximum 7x7 window!
    median_size = min(median_size, 7)
    cv2.imshow('Original', image)
    # apply the (median_size X median_size) median filter on the image [default 5 x 5]
    processed_image = cv2.medianBlur(image, median_size)
    # display image
    cv2.imshow('Median Filter Processing', processed_image)
    # pause the execution of the script until a key on the keyboard is pressed
    cv2.waitKey(0)


img = cv2.imread('training_data/001A942001B4A3-00103D5-001706C-001C4DB-0012F28001A0CA001F10F.jpg')
preprocess(img, 70)
