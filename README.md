# Shape Recognition

![Example 1](https://github.com/AbdelrahmanRadwan/object-detection/blob/master/results/example1.png  "Example 1")

![Example 2](https://github.com/AbdelrahmanRadwan/object-detection/blob/master/results/example2.png  "Example 2")


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
python3 shapes_counter.py -i training_data/001979900122A9-0017558-00101E4-001F3DE-00118C8001FC1B0016C37.jpg
```

## Algorithm
1. Do image preprocessing and reduce the noise.
2. Select the contours from the image.
3. Select the core approximate corners from each contour.
4. Determine the shape of the main contour; based on its number of vertices.
5. Draw the picture with its shapes tagged by their types.
6. Count the shapes occupancies and print the numbers, comma separated.

## Results
The results are not bad at all! a lot of test cases gonna be true, the algorithm can pass a lot of corner cases.

![Example 1](https://github.com/AbdelrahmanRadwan/object-detection/blob/master/results/1.png  "Example 1") ![Example 2](https://github.com/AbdelrahmanRadwan/object-detection/blob/master/results/2.png  "Example 2")
![Example 3](https://github.com/AbdelrahmanRadwan/object-detection/blob/master/results/3.png  "Example 3") ![Example 4](https://github.com/AbdelrahmanRadwan/object-detection/blob/master/results/4.png  "Example 4")
![Example 5](https://github.com/AbdelrahmanRadwan/object-detection/blob/master/results/5.png  "Example 5") ![Example 6](https://github.com/AbdelrahmanRadwan/object-detection/blob/master/results/6.png  "Example 6")
![Example 7](https://github.com/AbdelrahmanRadwan/object-detection/blob/master/results/7.png  "Example 7") ![Example 8](https://github.com/AbdelrahmanRadwan/object-detection/blob/master/results/8.png  "Example 8")


On the other side, the algorithm fails sometimes in the pics with small shapes (very small) or the unioned shapes.

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

