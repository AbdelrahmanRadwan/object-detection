#Reference: https://code.tutsplus.com/tutorials/image-filtering-in-python--cms-29202
import cv2

# Median filter
def preprocess(image, median_size=5):
    # It supports maximum 7x7 window!
    median_size = min(median_size, 7)
    # apply the (median_size X median_size) median filter on the image [default 5 x 5]
    processed_image = cv2.medianBlur(image, median_size)

    # pause the execution of the script until a key on the keyboard is pressed
    cv2.waitKey(0)
    return processed_image
