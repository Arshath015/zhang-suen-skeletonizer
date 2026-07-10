import cv2
import numpy as np

class DataIO:
    def __init__(self):
        pass
    def read_image(self, filename: str) -> np.ndarray:
        return cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    def write_image(self, filename: str, image: np.ndarray) -> None:
        cv2.imwrite(filename, image)