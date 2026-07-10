import pytest
from data_io import DataIO
import cv2
import numpy as np

def test_read_image():
    # Read a test image
    data_io = DataIO()
    image = data_io.read_image('test_image.png')
    assert image is not None

def test_write_image():
    # Write a test image
    data_io = DataIO()
    image = np.zeros((100, 100), dtype=np.uint8)
    data_io.write_image('test_output.png', image)
    assert cv2.imread('test_output.png', cv2.IMREAD_GRAYSCALE) is not None