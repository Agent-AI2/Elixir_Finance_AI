from pathlib import Path
from PIL import Image

from ingestion.ocr_reader import OCRReader
from ingestion.image_preprocessor import ImagePreprocessor


IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png"
}


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

processor = ImagePreprocessor()

image = processor.preprocess(image)

reader = OCRReader()

blocks = reader.read(image)

print(
    f"\nDetected {len(blocks)} text block(s).\n"
)

for block in blocks[:20]:
    print(block)