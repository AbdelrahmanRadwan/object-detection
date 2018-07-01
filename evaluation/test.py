"""
A simple tester for the algorithm.
Set the image url in the "image_url" variable below, then the algorithm goes through the shapes counting phases:
1. Do image preprocessing and reduce the noise.
2. Select the contours from the image.
3. Select the core approximate corners from each contour.
4. Determine the shape of the main contour; based on its number of vertices.
5. Draw the picture with its shapes tagged by their types.
6. Count the shapes occupancies and print the numbers, comma separated.
"""

import cv2
from contours_detection import get_contours
from shape_detector import ShapeDetector

def count_shapes(image, median_size=5):
    """
    :param image: The original image, in which you wanna reduce the noise.
    :param median_size: the matrix dimensions of the median filter
    :return: numpy array includes the contours in this image
    :draw: the original image with the contours detected and drawn on it and the names of each object in the picture.
    :print: the number of squares, circles and triangles in the image.
    """
    shapes = {
        "square": 0,
        "circle": 0,
        "triangle": 0,
        "rectangle": 0
    }

    shape_detector = ShapeDetector()

    contours = get_contours(image, median_size)

    #delete the boarder if it was added in the contours
    if contours[-1][0][0][0] == 0 and contours[-1][0][0][1] == 0 and contours[-1][-1][0][1] == 0:
        contours = contours[0:-1]

    for contour in contours:
        # compute the center of the contour, then detect the name of the shape using only the contour

        moments = cv2.moments(contour)
        # If the shape is so small (it's just a noise), skip it.
        if moments["m00"] <= 0.0:
            continue

        contourX = int((moments["m10"] / moments["m00"]))
        contourY = int((moments["m01"] / moments["m00"]))

        shape = shape_detector.detect(contour)
        shapes[shape] += 1

        cv2.drawContours(image, [contour],
                         -1, (0, 255, 0), 2)
        cv2.putText(image, shape, (contourX, contourY),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 0, 0), 2)

    print("squares: %d,\ncircles: %d,\ntriangle: %d"
          % (shapes["square"], shapes["circle"], shapes["triangle"]))
    cv2.imshow('img', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_url = '../training_data/001979900122A9-0017558-00101E4-001F3DE-00118C8001FC1B0016C37.jpg'

image = cv2.imread(image_url)
count_shapes(image, 7)