from pathlib import Path

from ingestion.page_assembler import PageAssembler

assembler = PageAssembler()

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}

files = sorted(
    f for f in Path("samples").iterdir()
    if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS
)

pages = assembler.assemble(files)

print()

for i, page in enumerate(pages, start=1):

    print(f"Logical Page {i}")

    for image in page:

        print("   ", image.name)

    print()