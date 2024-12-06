import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def compare_images(image1, image2):
    # Load images
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    if img1 is None:
        raise FileNotFoundError(f"Image not found or cannot be loaded: {image1}")
    if img2 is None:
        raise FileNotFoundError(f"Image not found or cannot be loaded: {image2}")

    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2_resized, cv2.COLOR_BGR2GRAY)

    ssim_score, _ = ssim(gray1, gray2, full=True)

    diff = cv2.absdiff(img1, img2_resized)

    total_pixels = img1.shape[0] * img1.shape[1] * 3  
    different_pixels = np.count_nonzero(diff)
    pixel_diff_percentage = (different_pixels / total_pixels) * 100
    similarity = (ssim_score * 100 + (100 - pixel_diff_percentage)) / 2
    return similarity, ssim_score, pixel_diff_percentage

image1_path = "./ss6.png"
image2_path = "./ss7.png"

try:
    similarity, ssim_score, pixel_diff = compare_images(image1_path, image2_path)
    print(f"Overall similarity: {similarity:.2f}%")
    print(f"SSIM score: {ssim_score:.4f}")
    print(f"Pixel difference: {pixel_diff:.2f}%")
except FileNotFoundError as e:
    print(e)
