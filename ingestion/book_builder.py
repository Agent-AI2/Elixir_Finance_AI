import json
from pathlib import Path
from PIL import Image

from ingestion.page_assembler import PageAssembler
from ingestion.image_preprocessor import ImagePreprocessor
from ingestion.document_cleaner import DocumentCleaner
from ingestion.ocr_reader import OCRReader
from ingestion.table_detector import TableDetector
from ingestion.cell_extractor import CellExtractor
from ingestion.capture_assistant import CaptureAssistant


class BookBuilder:

    def __init__(
        self,
        profile="custom",
        rotate_images=None,
        rotation_angle=None,
        merge_direction=None,
        preview_required=False,
        expected_columns=None,
        expected_rows=None
    ):

        self.profile = profile
        self.rotate_images = rotate_images
        self.rotation_angle = rotation_angle
        self.merge_direction = merge_direction
        self.preview_required = preview_required

        self.expected_columns = expected_columns
        self.expected_rows = expected_rows

        self.assembler = PageAssembler()
        self.preprocessor = ImagePreprocessor()
        self.cleaner = DocumentCleaner()
        self.ocr_reader = OCRReader()
        self.table_detector = TableDetector()
        self.cell_extractor = CellExtractor()

        self._load_profile()

    def _load_profile(self):

        try:

            with open(
                "configs/document_profiles.json",
                "r"
            ) as f:

                profiles = json.load(f)

            profile = profiles.get(
                self.profile,
                {}
            )

            if self.rotate_images is None:
                self.rotate_images = profile.get(
                    "rotate_before_merge",
                    False
                )

            if self.rotation_angle is None:
                self.rotation_angle = profile.get(
                    "rotation_angle",
                    0
                )

            if self.merge_direction is None:
                self.merge_direction = profile.get(
                    "merge_direction",
                    "horizontal"
                )

        except FileNotFoundError:

            self.rotate_images = False
            self.rotation_angle = 0
            self.merge_direction = "horizontal"

    def build(self, image_files):

        logical_pages = self.assembler.assemble(
            image_files
        )

        draft_book = []

        assistant = CaptureAssistant()

        for page_number, page_images in enumerate(
            logical_pages,
            start=1
        ):

            while True:

                merged_image = self._merge_images(
                    page_images
                )

                preview_path = (
                    f"outputs/merged_page_{page_number}.jpg"
                )

                merged_image.save(
                    preview_path
                )

                if not self.preview_required:
                    break

                confirmed = (
                    assistant.confirm_preview(
                        preview_path
                    )
                )

                if confirmed:
                    break

                correction = (
                    assistant.get_correction()
                )

                if correction == "1":
                    self.rotate_images = False

                elif correction == "2":
                    self.rotate_images = True
                    self.rotation_angle = 90

                elif correction == "3":
                    self.rotate_images = True
                    self.rotation_angle = -90

                elif correction == "4":
                    self.rotate_images = True
                    self.rotation_angle = 180

                elif correction == "5":

                    if self.merge_direction == "horizontal":
                        self.merge_direction = "vertical"
                    else:
                        self.merge_direction = "horizontal"

                elif correction == "6":

                    raise Exception(
                        "Processing cancelled by user."
                    )

            # -----------------------------------
            # Document Cleaning
            # -----------------------------------

            cleaned_image = self.cleaner.clean(
                merged_image
            )

            # -----------------------------------
            # OCR Preprocessing
            # -----------------------------------

            processed_image = (
                self.preprocessor.preprocess(
                    cleaned_image
                )
            )

            # -----------------------------------
            # OCR Processing
            # -----------------------------------

            text_blocks = (
                self.ocr_reader.read(
                    processed_image
                )
            )

            # -----------------------------------
            # Table Detection
            # -----------------------------------

            table_result = (
                self.table_detector.detect(
                    processed_image
                )
            )

            vertical_lines = (
                table_result.get(
                    "vertical_lines",
                    []
                )
            )

            horizontal_lines = (
                table_result.get(
                    "horizontal_lines",
                    []
                )
            )

            # -----------------------------------
            # Cell Extraction
            # -----------------------------------

            cells = (
                self.cell_extractor.extract(
                    vertical_lines,
                    horizontal_lines
                )
            )

            page = {

                "page_number":
                    page_number,

                "source_files": [
                    Path(
                        p
                    ).name
                    for p in page_images
                ],

                "image_width":
                    merged_image.width,

                "image_height":
                    merged_image.height,

                "text_blocks":
                    text_blocks,

                "vertical_lines":
                    vertical_lines,

                "horizontal_lines":
                    horizontal_lines,

                "cells":
                    cells,

                "expected_columns":
                    self.expected_columns,

                "expected_rows":
                    self.expected_rows,

                "columns": [],

                "rows": [],

                "status":
                    "Draft"
            }

            draft_book.append(
                page
            )

        return draft_book

    def _merge_images(
        self,
        image_paths
    ):

        images = []

        for image_path in image_paths:

            img = Image.open(
                image_path
            )

            if self.rotate_images:

                img = img.rotate(
                    self.rotation_angle,
                    expand=True
                )

            images.append(
                img
            )

        # -----------------------------------
        # Horizontal Merge
        # -----------------------------------

        if self.merge_direction == "horizontal":

            total_width = sum(
                img.width
                for img in images
            )

            max_height = max(
                img.height
                for img in images
            )

            merged = Image.new(
                "RGB",
                (
                    total_width,
                    max_height
                ),
                "white"
            )

            x_offset = 0

            for img in images:

                merged.paste(
                    img,
                    (
                        x_offset,
                        0
                    )
                )

                x_offset += img.width

        # -----------------------------------
        # Vertical Merge
        # -----------------------------------

        else:

            max_width = max(
                img.width
                for img in images
            )

            total_height = sum(
                img.height
                for img in images
            )

            merged = Image.new(
                "RGB",
                (
                    max_width,
                    total_height
                ),
                "white"
            )

            y_offset = 0

            for img in images:

                merged.paste(
                    img,
                    (
                        0,
                        y_offset
                    )
                )

                y_offset += img.height

        return merged