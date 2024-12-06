"""import cv2
import os

def compare_images(image1, image2):
    # Load images
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    # Resize images to have the same dimensions
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Compute absolute difference
    diff = cv2.absdiff(img1, img2_resized)
    
    # Split the difference image into channels
    b, g, r = cv2.split(diff)
    
    # Count non-zero pixels in each channel
    b_non_zero = cv2.countNonZero(b)
    g_non_zero = cv2.countNonZero(g)
    r_non_zero = cv2.countNonZero(r)
    
    # Calculate total non-zero pixels
    total_non_zero = b_non_zero + g_non_zero + r_non_zero
    
    # Calculate percentage similarity
    total_pixels = img1.shape[0] * img1.shape[1] * 3  # Multiply by 3 for 3 channels
    similarity = (1 - (total_non_zero / total_pixels)) * 100
    return similarity

def compare_all_images():
    solved_folder = "./solved"
    answers_folder = "./answers"

    solved_images = os.listdir(solved_folder)
    answers_images = os.listdir(answers_folder)

    solved_images.sort()
    answers_images.sort()

    for solved_image, answer_image in zip(solved_images, answers_images):
        solved_image_path = os.path.join(solved_folder, solved_image)
        answer_image_path = os.path.join(answers_folder, answer_image)
        similarity_percentage = compare_images(solved_image_path, answer_image_path)
        print(f"Similarity percentage between {solved_image} and {answer_image}: {similarity_percentage:.2f}%")

compare_all_images()


# # Test the function
image1_path = "./Screenshot (991).png"
image2_path = "./Screenshot (990).png"

similarity_percentage = compare_images(image1_path, image2_path)
print("Similarity percentage:", similarity_percentage)"""

"""
import cv2
import os

def compare_images(image1, image2):
    # Load images
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    
    # Resize images to have the same dimensions
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    
    # Compute absolute difference
    diff = cv2.absdiff(img1, img2_resized)
    
    # Split the difference image into channels
    b, g, r = cv2.split(diff)
    
    # Count non-zero pixels in each channel
    b_non_zero = cv2.countNonZero(b)
    g_non_zero = cv2.countNonZero(g)
    r_non_zero = cv2.countNonZero(r)
    
    # Calculate total non-zero pixels
    total_non_zero = b_non_zero + g_non_zero + r_non_zero
    
    # Calculate percentage similarity
    total_pixels = img1.shape[0] * img1.shape[1] * 3  # Multiply by 3 for 3 channels
    similarity = (1 - (total_non_zero / total_pixels)) * 100
    return similarity

# Test the function with the two screenshots
image1_path = "./image.png"
image2_path = "./Screenshot (995).png"

similarity_percentage = compare_images(image1_path, image2_path)
print(f"Similarity percentage between the two screenshots: {similarity_percentage:.2f}%")"""

import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def compare_images(image1, image2):
    # Load images
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    
    # Resize images to have the same dimensions
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    
    # Convert images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2_resized, cv2.COLOR_BGR2GRAY)
    
    # Compute SSIM between the two images
    ssim_score, _ = ssim(gray1, gray2, full=True)
    
    # Compute absolute difference
    diff = cv2.absdiff(img1, img2_resized)
    
    # Calculate percentage of different pixels
    total_pixels = img1.shape[0] * img1.shape[1] * 3
    different_pixels = np.count_nonzero(diff)
    pixel_diff_percentage = (different_pixels / total_pixels) * 100
    
    # Combine SSIM and pixel difference for final similarity score
    similarity = (ssim_score * 100 + (100 - pixel_diff_percentage)) / 2
    
    return similarity, ssim_score, pixel_diff_percentage

# Test the function with the two screenshots
image1_path = "./image.png"
image2_path = "./Screenshot (995).png"

similarity, ssim_score, pixel_diff = compare_images(image1_path, image2_path)
print(f"Overall similarity: {similarity:.2f}%")
print(f"SSIM score: {ssim_score:.4f}")
print(f"Pixel difference: {pixel_diff:.2f}%")