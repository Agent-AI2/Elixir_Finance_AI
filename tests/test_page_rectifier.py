from PIL import Image
import cv2

from ingestion.page_rectifier import (
    PageRectifier
)

image = Image.open(
    "outputs/cleaned_page.jpg"
)

rectifier = PageRectifier()

rectified, angle = rectifier.rectify(
    image
)

cv2.imwrite(
    "outputs/rectified_page.jpg",
    rectified
)

print(
    "\nPage rectified successfully."
)

print(
    f"Detected angle: {angle:.2f}"
)

print(
    "Saved to:"
)

print(
    "outputs/rectified_page.jpg"
)