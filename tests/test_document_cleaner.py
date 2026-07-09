from pathlib import Path
from PIL import Image
import cv2

from ingestion.document_cleaner import (
    DocumentCleaner
)

image_path = (
    "outputs/merged_page_1.jpg"
)

image = Image.open(
    image_path
)

cleaner = DocumentCleaner()

cleaned = cleaner.clean(
    image
)

cv2.imwrite(
    "outputs/cleaned_page.jpg",
    cleaned
)

print(
    "\nDocument cleaned successfully."
)

print(
    "Saved to:"
)

print(
    "outputs/cleaned_page.jpg"
)