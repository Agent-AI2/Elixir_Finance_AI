from pathlib import Path

from ingestion.document_detector import (
    DocumentDetector
)


class ElixirFinanceAI:

    def process(
        self,
        input_file
    ):

        detector = (
            DocumentDetector()
        )

        result = detector.process(
            Path(input_file)
        )

        # ----------------------------------
        # Bank statement workflow
        # ----------------------------------

        if isinstance(result, list):

            # Digital account book pages
            if (
                len(result) > 0 and
                isinstance(result[0], dict) and
                "page_number" in result[0]
            ):

                for page in result:

                    print(
                        "\nDraft Digital Account Book Created\n"
                    )

                    print(
                        f"Page Number      : "
                        f"{page['page_number']}"
                    )

                    print(
                        f"Source Files     : "
                        f"{page['source_files']}"
                    )

                    print(
                        f"Image Size       : "
                        f"{page['image_width']} x "
                        f"{page['image_height']}"
                    )

                    print(
                        f"Text Blocks      : "
                        f"{len(page.get('text_blocks', []))}"
                    )

                    print(
                        f"Vertical Lines   : "
                        f"{len(page.get('vertical_lines', []))}"
                    )

                    print(
                        f"Horizontal Lines : "
                        f"{len(page.get('horizontal_lines', []))}"
                    )

                    print(
                        f"Cells Extracted  : "
                        f"{len(page.get('cells', []))}"
                    )

                    print(
                        f"Status           : "
                        f"{page['status']}"
                    )

                    print(
                        "-" * 50
                    )

            # Transaction extraction workflow
            else:

                print(
                    f"\nExtracted "
                    f"{len(result)} "
                    f"transactions."
                )

        return result