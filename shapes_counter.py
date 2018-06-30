import cv2
from contours_detection import get_contours
from shape_detector import ShapeDetector


image = cv2.imread('training_data/001EE370015D7B-001B514-001AF1A-001D2BD-001E41B001061C001D292.jpg')

sd = ShapeDetector()
contours = get_contours(image)
# loop over the contours

#delete the boarder if it was added in the contours
if contours[-1][0][0][0] == 0 and contours[-1][0][0][1] == 0 and contours[-1][-1][0][1] == 0:
    contours = contours[0:-1]

for c in contours:
    # compute the center of the contour, then detect the name of the
    # shape using only the contour
    M = cv2.moments(c)
    if M["m00"] <= 0.0:
        continue
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))

    shape = sd.detect(c)
    print(shape)
    # multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image
    c = c.astype("float")
    c = c.astype("int")
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 255, 255), 2)

cv2.imshow('img',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
