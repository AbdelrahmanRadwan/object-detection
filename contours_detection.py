"""
This file includes an Algorithm to extract the contours from an image.

Reference: https://www.youtube.com/watch?v=hrwsHlKqBRw
"""
import cv2
from preprocessing import preprocess


def get_contours(image, median_size=5):
    """
    :param image: The original image, in which you wanna reduce the noise.
    :param median_size: the matrix dimensions of the median filter
    :return: numpy array includes the contous in this image
    :draw: the original image with the contous detected and drawn on it
    """
    image_with_noise = image
    image = preprocess(image, median_size)

    blurred = cv2.pyrMeanShiftFiltering(image, 31, 91)

    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #ret, threshold = cv2.threshold(gray, 127, 255, 1)

    _, contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    #_, contours, _ = cv2.findContours(threshold,1,2)

    cv2.drawContours(image_with_noise, contours, -1, (0, 0, 255), 6)

    cv2.namedWindow("Contours Detection", cv2.WINDOW_NORMAL)
    cv2.imshow("Contours Detection", image_with_noise)
    cv2.waitKey()
    return contours
