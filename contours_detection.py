#Reference: https://www.youtube.com/watch?v=hrwsHlKqBRw
import cv2
from preprocessing import preprocess


def get_contours(image):
    img = image
    image = preprocess(image, 5)

    blurred = cv2.pyrMeanShiftFiltering(image, 31, 91)

    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
   #ret, threshold = cv2.threshold(gray, 127, 255, 1)

    _, contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    #_, contours, _ = cv2.findContours(threshold,1,2)

    cv2.drawContours(img, contours, -1, (0, 0, 255), 6)

    cv2.namedWindow("Display", cv2.WINDOW_NORMAL)
    cv2.imshow("Display", img)
    cv2.waitKey()
    return contours


#image = cv2.imread('training_data/001A1FE001CDDE-0014160-0011C03-0017ED2-001229D0012A16001956E.jpg')
#print(get_contours(image))