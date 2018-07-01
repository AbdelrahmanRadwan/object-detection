# Shape Recognition

![Example 1](https://raw.github.com/AbdelrahmanRadwan/object-detection/tree/master/evaluation/example2.png  "Example 2")
![Example 2](https://raw.github.com/AbdelrahmanRadwan/object-detection/tree/master/evaluation/example1.png  "Example 1")
A tool used for recognising and counting the number of occurrences
 of three different shapes (i.e. square, circle, triangle) in a given image. 
 [Easily scalable in terms of new shapes]

The tool takes an image path as input, and returns three
 comma separated integers separated with as output:
```
<int>,<int>,<int>
```
Where the first integer corresponds to the number of **squares**
 in the image, the second integer corresponds to the number of **circles**,
  and the third integer corresponds to the number of **triangles**.

## How to Run
```
python3 shapes_counter.py -i <image_path>
```
##### example:
```bash
python3 shapes_counter.py -i training_data/001EE370015D7B-001B514-001AF1A-001D2BD-001E41B001061C001D292.jpg
```

## Algorithm
1. Do image preprocessing and reduce the noise.
2. Select the contours from the image.
3. Select the core approximate corners from each contour.
4. Determine the shape of the main contour; based on its number of vertices.
5. Draw the picture with its shapes tagged by their types.
6. Count the shapes occupancies and print the numbers, comma separated.

## Results


## Furthur work
1. 

## References
- Tried image denoising, but didn't work well:
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_photo/py_non_local_means/py_non_local_means.html

- Tried Canny edge detection didn't work well:
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html

- tried the lovcal mean also, didn't work well:
http://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Non-local_Means_Denoising_Algorithm_Noise_Reduction.php

- Preprocessing: https://code.tutsplus.com/tutorials/image-filtering-in-python--cms-29202

- contours detection: Reference: https://www.youtube.com/watch?v=hrwsHlKqBRw

