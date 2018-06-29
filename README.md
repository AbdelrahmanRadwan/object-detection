# Shape Recognition Challenge

## Deadline
You have 48 hours to solve this challenge (from the time you received this document). Please keep in mind that a solution to this problem can be implemented in a handful of hours but the idea is to give you extra time in case you want to go further.

## Goal
The goal is to implement an algorithm to recognise and count the number of occurrence of three different shapes (i.e. square, circle, triangle) in a given image.

Your algorithm must take an image path as input:
```
cool_algorithm.py <image path string>
```
And return three integers separated with commas (in a string) as output:
```
<int>,<int>,<int>
```
Where the first integer corresponds to the number of **squares** in the image, the second integer corresponds to the number of **circles**, and the third integer corresponds to the number of **triangles**.

Example:
Using the following image as input:
```
cool_algorithm.py ./training_data/example_image.jpg
```
Expected output:
```
3,1,2
```
When the image contains 3 squares, 1 circle, and 2 triangles.

## Restrictions
There are no restrictions on the approach to use to solve this problem and you are free to use the method of your choice (e.g. hard-coded logic, image processing heuristics, shallow machine learning, deep learning, etc). The only restriction is to implement your algorithm using Python and you are only allowed the use the following set of libraries since we want to be able to run your code at the end.
* Numpy
* OpenCV2
* Pillow
* Scipy
* Scikit-learn
* NLTK
* Keras
* Tensorflow
* PyTorch
* Theano

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
