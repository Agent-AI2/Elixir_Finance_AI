from pathlib import Path
from PIL import Image
import cv2

from ingestion.table_detector import TableDetector
from ingestion.image_preprocessor import (
    ImagePreprocessor
)


image_path = (
    "outputs/ocr_input_page_1.jpg"
)

image = Image.open(
    image_path
)

preprocessor = (
    ImagePreprocessor()
)

processed = (
    preprocessor.preprocess(
        image
    )
)

detector = TableDetector()

result = detector.detect(
    processed
)

print(
    f"\nDetected "
    f"{len(result['vertical_lines'])} "
    f"vertical lines."
)

print(
    f"Detected "
    f"{len(result['horizontal_lines'])} "
    f"horizontal lines."
)

cv2.imwrite(
    "outputs/vertical_lines.jpg",
    result["vertical_image"]
)

cv2.imwrite(
    "outputs/horizontal_lines.jpg",
    result["horizontal_image"]
)

print(
    "\nSaved:"
)

print(
    "outputs/vertical_lines.jpg"
)

print(
    "outputs/horizontal_lines.jpg"
)