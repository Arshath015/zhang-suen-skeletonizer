from typing import Tuple
import cv2
import numpy as np

class Skeletonizer:
    def __init__(self):
        pass
    def skeletonize(self, image: np.ndarray) -> np.ndarray:
        # Apply thresholding to the input image
        _, thresholded_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # Initialize the output skeleton
        output_skeleton = thresholded_image.copy()
        # Apply the Zhang-Suen skeletonization algorithm
        while True:
            # First sub-iteration
            marked_for_deletion = self.first_sub_iteration(output_skeleton)
            if np.sum(marked_for_deletion) == 0:
                break
            output_skeleton[marked_for_deletion] = 0
            # Second sub-iteration
            marked_for_deletion = self.second_sub_iteration(output_skeleton)
            if np.sum(marked_for_deletion) == 0:
                break
            output_skeleton[marked_for_deletion] = 0
        return output_skeleton
    def first_sub_iteration(self, image: np.ndarray) -> np.ndarray:
        marked_for_deletion = np.zeros_like(image)
        for i in range(1, image.shape[0] - 1):
            for j in range(1, image.shape[1] - 1):
                if self.check_conditions(image, i, j):
                    marked_for_deletion[i, j] = 1
        return marked_for_deletion
    def second_sub_iteration(self, image: np.ndarray) -> np.ndarray:
        marked_for_deletion = np.zeros_like(image)
        for i in range(1, image.shape[0] - 1):
            for j in range(1, image.shape[1] - 1):
                if self.check_conditions(image, i, j):
                    marked_for_deletion[i, j] = 1
        return marked_for_deletion
    def check_conditions(self, image: np.ndarray, i: int, j: int) -> bool:
        # Check conditions for the pixel (i, j)
        if not (2 <= self.count_neighbors(image, i, j) <= 6):
            return False
        if not self.is_single(image, i, j):
            return False
        if not self.check_N_W_E_S(image, i, j):
            return False
        return True
    def count_neighbors(self, image: np.ndarray, i: int, j: int) -> int:
        count = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                if 0 <= i + x < image.shape[0] and 0 <= j + y < image.shape[1] and image[i + x, j + y] == 255:
                    count += 1
        return count
    def is_single(self, image: np.ndarray, i: int, j: int) -> bool:
        return image[i, j] == 255
    def check_N_W_E_S(self, image: np.ndarray, i: int, j: int) -> bool:
        return image[i - 1, j] == 0 and image[i, j - 1] == 0 and image[i, j + 1] == 0 and image[i + 1, j] == 0