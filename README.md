# Zhang-Suen Skeletonization for Image Processing
[![PyPI version](https://badge.fury.io/py/zhang-suen-skeletonizer.svg)](https://pypi.org/project/zhang-suen-skeletonizer)
[![Build Status](https://travis-ci.org/your-username/zhang-suen-skeletonizer.svg?branch=main)](https://travis-ci.org/your-username/zhang-suen-skeletonizer)
## Overview
A Python submodule implementing the Zhang-Suen skeletonization technique for extracting the skeletal structure from binary images.
## Tech Stack
* Python 3.8+
* OpenCV 4.5+
* NumPy 1.20+
## Architecture
```
+---------------+
|  Input Image  |
+---------------+
       |
       |
       v
+---------------+
|  Preprocessing  |
|  (Thresholding)  |
+---------------+
       |
       |
       v
+---------------+
| Zhang-Suen      |
|  Skeletonization |
+---------------+
       |
       |
       v
+---------------+
|  Output Skeleton|
+---------------+
```
## Theoretical Background
The Zhang-Suen skeletonization technique is an iterative algorithm that removes pixels from the boundaries of an object in a binary image while preserving the shape and connectivity of the object. The algorithm consists of two sub-iterations. The first sub-iteration checks the following conditions for a pixel p:
* 2 \u2264 N(p) \u2264 6
* S(p) = 1
* p \* (N(p) = 6) = 0
* (p \* (N(p) = 6) \* (N(p \* W) \* (N(p \* E) \* (N(p \* S)))) = 0
If all these conditions are met, the pixel p is marked for deletion. The second sub-iteration checks similar conditions for the pixels marked for deletion in the first sub-iteration. The algorithm continues until no more pixels are marked for deletion.
## Installation
`pip install zhang-suen-skeletonizer`
## Usage
```python
from zhang_suen_skeletonizer import Skeletonizer
skeletonizer = Skeletonizer()
input_image = cv2.imread('input_image.png', cv2.IMREAD_GRAYSCALE)
output_skeleton = skeletonizer.skeletonize(input_image)
```
## Limitations
The algorithm assumes that the input image is a binary image. If the input image is not binary, the algorithm may not produce the expected results.
## Roadmap
* Improve the performance of the algorithm for large images
* Add support for color images
## License
The Zhang-Suen Skeletonizer is licensed under the MIT License.