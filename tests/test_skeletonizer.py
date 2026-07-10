import pytest
from zhang_suen_skeletonizer import Skeletonizer
import cv2
import numpy as np

def test_skeletonizer_simple_image():
    # Create a simple image with a single object
    image = np.zeros((100, 100), dtype=np.uint8)
    image[10:20, 10:20] = 255
    skeletonizer = Skeletonizer()
    output_skeleton = skeletonizer.skeletonize(image)
    assert np.sum(output_skeleton) > 0

def test_skeletonizer_empty_image():
    # Create an empty image
    image = np.zeros((100, 100), dtype=np.uint8)
    skeletonizer = Skeletonizer()
    output_skeleton = skeletonizer.skeletonize(image)
    assert np.sum(output_skeleton) == 0