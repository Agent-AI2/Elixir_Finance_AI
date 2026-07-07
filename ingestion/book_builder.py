from pathlib import Path
from PIL import Image

from ingestion.page_assembler import PageAssembler


class BookBuilder:
    """
    Creates draft digital account books from one or more screenshots.
    """

    def __init__(self):

        self.assembler = PageAssembler()

    def build(self, image_files):

        logical_pages = self.assembler.assemble(image_files)

        draft_book = []

        for page_number, page_images in enumerate(logical_pages, start=1):

            merged = self._merge_images(page_images)

            draft_book.append(

                self._create_page(
                    page_number,
                    page_images,
                    merged
                )

            )

        return draft_book

    # -----------------------------------------
    # Merge all screenshots belonging to a page
    # -----------------------------------------

    def _merge_images(self, image_paths):

        images = []

        total_width = 0

        max_height = 0

        for image_path in image_paths:

            img = Image.open(image_path)

            images.append(img)

            total_width += img.width

            max_height = max(max_height, img.height)

        merged = Image.new(
            "RGB",
            (total_width, max_height),
            "white"
        )

        x = 0

        for img in images:

            merged.paste(img, (x, 0))

            x += img.width

        return merged

    # -----------------------------------------
    # Create one draft page
    # -----------------------------------------

    def _create_page(
        self,
        page_number,
        page_images,
        merged_image
    ):

        return {

            "page_number": page_number,

            "source_files": [
                Path(p).name
                for p in page_images
            ],

            "status": "Draft",

            "image_width": merged_image.width,

            "image_height": merged_image.height,

            "merged_image": merged_image,

            "columns": [],

            "rows": []

        }