from zhang_suen_skeletonizer import Skeletonizer
import cv2

# Create a skeletonizer
skeletonizer = Skeletonizer()
# Read an input image
input_image = cv2.imread('input_image.png', cv2.IMREAD_GRAYSCALE)
# Apply the Zhang-Suen skeletonization algorithm
output_skeleton = skeletonizer.skeletonize(input_image)
# Display the output skeleton
cv2.imshow('Output Skeleton', output_skeleton)
 cv2.waitKey(0)
 cv2.destroyAllWindows()