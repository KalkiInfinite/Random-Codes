import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter('ignore', Image.DecompressionBombWarning)
Image.MAX_IMAGE_PIXELS = None

quantization_table = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
])

def split_into_blocks(image_matrix):
    h, w = image_matrix.shape
    blocks = []
    for i in range(0, h, 8):
        for j in range(0, w, 8):
            block = image_matrix[i:i+8, j:j+8]
            if block.shape == (8, 8):
                blocks.append(block)
    return blocks

def rgb_to_ycbcr(image):
    return image.convert('YCbCr')

def dct_2d(block):
    max_value = np.max(block)
    max_value = np.clip(max_value, a_min=1, a_max=None)
    return np.round(np.fft.fft2(block) * 255 / max_value)

def quantize_block(block, quantization_table):
    return np.round(block / quantization_table)

def zigzag_scan(block):
    zigzag_pattern = []
    for i in range(0, 8):
        if i % 2 == 0:
            zigzag_pattern.extend(block[i][:i+1])
        else:
            zigzag_pattern.extend(np.flip(block[i][:i+1]))
    return zigzag_pattern

def dpcm_encode(blocks):
    dc_elements = [block[0, 0] for block in blocks]
    diffs = np.diff(dc_elements)
    return diffs

def rle_encode(data):
    encoding = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        encoding.append((data[i], count))
        i += 1
    return encoding

def jpeg_compression(image_path):
    image = Image.open(image_path)
    image_ycbcr = rgb_to_ycbcr(image)
    image_matrix = np.array(image_ycbcr)[:, :, 0]

    original_size = image.size[0] * image.size[1]
    blocks = split_into_blocks(image_matrix)
    dct_blocks = [dct_2d(block) for block in blocks]
    quantized_blocks = [quantize_block(block, quantization_table) for block in dct_blocks]
    zigzag_scanned = [zigzag_scan(block) for block in quantized_blocks]
    dpcm_encoded = dpcm_encode(quantized_blocks)
    rle_encoded = [rle_encode(block[1:]) for block in zigzag_scanned]

    compressed_size = sum(len(block) for block in rle_encoded) + len(dpcm_encoded)
    compression_factor = original_size / compressed_size if compressed_size != 0 else float('inf')

    print(f"Original Image Size (in pixels): {original_size} pixels")
    print(f"Compressed Image Size (approx.): {compressed_size} bytes")
    print(f"Compression Factor: {compression_factor:.2f}")

    return rle_encoded, dpcm_encoded

image_path = r"C:\Users\piyus\OneDrive\Desktop\ECESA\img\types.jpg"
jpeg_compression(image_path)
