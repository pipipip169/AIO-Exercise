# Read image

import numpy as np
import cv2

bg1_image = cv2.imread('D:/AIO/Draf/GreenBackground.png', 1)
ob_image = cv2.imread('D:/AIO/Draf/Object.png', 1)
bg2_image = cv2.imread('D:/AIO/Draf/NewBackground.jpg', 1)

# Resize image

IMAGE_SIZE = (678, 381)

bg1_image = cv2.resize(bg1_image, IMAGE_SIZE)
ob_image = cv2.resize(ob_image, IMAGE_SIZE)
bg2_image = cv2.resize(bg2_image, IMAGE_SIZE)

# Compute difference


def compute_difference(bg_img, input_img):
    difference_three_channels = cv2.absdiff(bg_img, input_img)
    difference_single_channels = np.sum(
        difference_three_channels, axis=2) / 3.0
    difference_single_channels = difference_single_channels.astype('uint8')

    return difference_single_channels


difference_single_channels = compute_difference(bg1_image, ob_image)
cv2.imshow('Difference single channels', difference_single_channels)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Compute Binary mask


def compute_binary_mask(difference_single_channels):
    difference_binary = np.where(
        difference_single_channels >= 15, 255, 0).astype('uint8')
    difference_binary = np.stack((difference_binary,) * 3, axis=-1)
    return difference_binary


binary_mask = compute_binary_mask(difference_single_channels)

cv2.imshow('Binary mask', binary_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Background subtraction


def background_subtraction(bg1_image, bg2_image, ob_image):
    difference_single_channels = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channels)
    output = np.where(binary_mask == 255, ob_image, bg2_image)
    return output


output = background_subtraction(bg1_image, bg2_image, ob_image)
cv2.imshow('Replace background', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
