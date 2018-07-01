"""
A simple visualization tool, to track the updates and changes in the pictures
"""
import cv2
import numpy as np

image_url = '../training_data/001A0A700122E3-001D292-0017D19-001F7A8-00143EE001FF85001BB81.jpg'
image = cv2.imread(image_url)

image_plot1 = image.copy()
image_plot2 = None
image_plot3 = None
image_plot4 = None
image_plot5 = None
image_plot6 = None


class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
        else:
            shape = "circle"
        return shape


def preprocess(image, median_size=5):
    median_size = min(median_size, 7)
    processed_image = cv2.medianBlur(image, median_size)
    return processed_image


def get_contours(image, median_size=5):
    global image_plot2, image_plot3, image_plot4, image_plot5
    image_with_noise = image.copy()
    image = preprocess(image, median_size)
    image_plot2 = image.copy()
    blurred = cv2.pyrMeanShiftFiltering(image, 31, 91)
    image_plot3 = blurred.copy()
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    image_plot4 = gray.copy()
    ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    _, contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    image_with_noise = image_plot3.copy()
    cv2.drawContours(image_with_noise, contours, -1, (0, 0, 255), 6)
    image_plot5 = image_with_noise.copy()
    return contours


def count_shapes(image, median_size=5):
    global image_plot6

    shape_detector = ShapeDetector()
    contours = get_contours(image, median_size)
    if contours[-1][0][0][0] == 0 and contours[-1][0][0][1] == 0 and contours[-1][-1][0][1] == 0:
        contours = contours[0:-1]
    for contour in contours:
        moments = cv2.moments(contour)
        if moments["m00"] <= 0.0:
            continue
        contourX = int((moments["m10"] / moments["m00"]))
        contourY = int((moments["m01"] / moments["m00"]))
        shape = shape_detector.detect(contour)
        cv2.drawContours(image, [contour],
                         -1, (0, 255, 0), 2)
        cv2.putText(image, shape, (contourX, contourY),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255), 2)
    image_plot6 = image.copy()


count_shapes(image)
image_plot1 = cv2.resize(image_plot1, (0, 0), None, .75, .75)
image_plot2 = cv2.resize(image_plot2, (0, 0), None, .75, .75)
image_plot3 = cv2.resize(image_plot3, (0, 0), None, .75, .75)
image_plot4 = cv2.resize(image_plot4, (0, 0), None, .75, .75)
image_plot5 = cv2.resize(image_plot5, (0, 0), None, .75, .75)
image_plot6 = cv2.resize(image_plot6, (0, 0), None, .75, .75)

numpy_horizontal_concat = np.concatenate((image_plot1, image_plot2, image_plot3,
                                          image_plot5, image_plot6, ), axis=1)
cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)
cv2.waitKey()