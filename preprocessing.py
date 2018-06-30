"""
This file includes preprocessing phase, to reduce the noise in the picture,
remove salt and pepper noise, and reduce the strength of the crossing lines.

Reference: https://code.tutsplus.com/tutorials/image-filtering-in-python--cms-29202
"""
import cv2

# Median filter
def preprocess(image, median_size=5):
    """
    :param image: The original image, in which you wanna reduce the noise.
    :param median_size: the matrix dimensions of the median filter
    :return: The cleaned image
    """
    # It supports maximum 7x7 window!
    median_size = min(median_size, 7)
    # apply the (median_size X median_size) median filter on the image [default 5 x 5]
    processed_image = cv2.medianBlur(image, median_size)
    return processed_image
