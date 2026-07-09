from pathlib import Path

from parsers.access_parser import (
    AccessBankParser
)

from ingestion.book_builder import (
    BookBuilder
)

from ingestion.capture_assistant import (
    CaptureAssistant
)


class DocumentDetector:

    def process(
        self,
        file_path
    ):

        suffix = (
            Path(file_path)
            .suffix
            .lower()
        )

        if suffix == ".pdf":

            parser = (
                AccessBankParser()
            )

            return (
                parser
                .extract_transactions(
                    file_path
                )
            )

        elif suffix in {
            ".jpg",
            ".jpeg",
            ".png"
        }:

            assistant = (
                CaptureAssistant()
            )

            settings = (
                assistant
                .get_profile()
            )

            builder = (
                BookBuilder(
                    **settings
                )
            )

            image_files = sorted(
                Path(
                    file_path
                ).parent.glob("*")
            )

            image_files = [

                f for f in image_files

                if f.suffix.lower()
                in {
                    ".jpg",
                    ".jpeg",
                    ".png"
                }
            ]

            return builder.build(
                image_files
            )

        raise ValueError(
            f"Unsupported file type: {suffix}"
        )