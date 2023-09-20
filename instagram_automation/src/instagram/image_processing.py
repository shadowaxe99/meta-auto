
import cv2
import numpy as np

def resize_image(image_path, size=(1080, 1080)):
    image = cv2.imread(image_path)
    image = cv2.resize(image, size)
    return image

def apply_filter(image, filter_name):
    if filter_name == 'grayscale':
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif filter_name == 'blur':
        return cv2.GaussianBlur(image, (15, 15), 0)
    else:
        return image

def save_image(image, save_path):
    cv2.imwrite(save_path, image)

def process_image(image_path, save_path, size=(1080, 1080), filter_name=None):
    image = resize_image(image_path, size)
    if filter_name:
        image = apply_filter(image, filter_name)
    save_image(image, save_path)

This is a simple image processing module using OpenCV. It includes functions to resize an image, apply a filter to an image, save an image, and a main process_image function that combines these steps.