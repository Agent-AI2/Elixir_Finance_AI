from pathlib import Path

from parsers.access_parser import AccessBankParser
from ingestion.book_builder import BookBuilder


class DocumentDetector:

    def process(self, file_path):

        file_path = Path(file_path)

        suffix = file_path.suffix.lower()

        if suffix == ".pdf":

            parser = AccessBankParser()

            return parser.extract_transactions(file_path)

        elif suffix in [".jpg", ".jpeg", ".png"]:

            folder = file_path.parent

            image_extensions = {".jpg", ".jpeg", ".png"}

            image_files = sorted(

                f for f in folder.iterdir()

                if f.is_file()

                and f.suffix.lower() in image_extensions

            )

            builder = BookBuilder()

            return builder.build(image_files)

        raise ValueError(
            f"Unsupported file type: {suffix}"
        )