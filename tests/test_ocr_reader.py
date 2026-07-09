from pathlib import Path
from PIL import Image

from ingestion.ocr_reader import OCRReader
from ingestion.image_preprocessor import ImagePreprocessor


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}

images = sorted(
    f for f in Path("samples").iterdir()
    if f.is_file()
    and f.suffix.lower() in IMAGE_EXTENSIONS
)

if not images:
    raise FileNotFoundError(
        "No image files found."
    )

image = Image.open(images[0])

# Create preprocessor
processor = ImagePreprocessor()

# Preprocess image
processed_image = processor.preprocess(image)

# Save for inspection
processed_image.save(
    "outputs/ocr_input.jpg"
)

# Create OCR reader
reader = OCRReader()

# OCR
blocks = reader.read(processed_image)

print(
    f"\nDetected {len(blocks)} text block(s).\n"
)

for block in blocks[:20]:
    print(block)