# Shape Recognition

## How to Run
```
python3 shapes_counter.py -i <image_path>
```
#### example:
```bash
python3 shapes_counter.py -i training_data/001EE370015D7B-001B514-001AF1A-001D2BD-001E41B001061C001D292.jpg
```

## Goal
The goal is to implement an algorithm to recognise and count the number of occurrence of three different shapes (i.e. square, circle, triangle) in a given image.

The algorithm takes an image path as input:
```
cool_algorithm.py <image path string>
```
And return three integers separated with commas (in a string) as output:
```
<int>,<int>,<int>
```
Where the first integer corresponds to the number of **squares** in the image, the second integer corresponds to the number of **circles**, and the third integer corresponds to the number of **triangles**.

## Dataset
In order to help you implement this algorithm, you can find 5000 annotated examples in the folder named training_data. The folder contains:
* JPG image of size 500 x 500 with arbitrary numbers of squares, circles, and triangles.
* Text file stating how many squares, circles, and triangles are in the image.
You are of course also free to create or use other examples if it helps.

## Evaluation
This is a hard problem so please don’t panic if your algorithm isn’t 100% accurate. The goal of this challenge is to assess your ability to provide a possible solution to a hard problem in a real-life scenario where you can work from the comfort of your home within a specified time window.

Your algorithm will be evaluated on 500 images that you do have access to.
The following metrics will be measured:
* Prediction accuracy shape-wise: accuracy over total number of successfully counted shapes in the evaluation set.
* Prediction accuracy image-wise: accuracy over total number of images where all shapes were successfully counted.

To hand-in your solution, please send an archive or a link to an archive (e.g. direct server link, Dropbox) with:
* Your Python file(s).
* Possible additional files.
* Optional instructions on how to run your solution.
By email to tony@uizard.io with the subject “Shape Recognition Challenge”. The total size of your solution must not exceed 950 MB.

Good luck and have fun! :)


## References
- Tried image denoising, but didn't work well:
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_photo/py_non_local_means/py_non_local_means.html

- Tried Canny edge detection didn't work well:
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html

- tried the lovcal mean also, didn't work well:
http://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Non-local_Means_Denoising_Algorithm_Noise_Reduction.php

- 
