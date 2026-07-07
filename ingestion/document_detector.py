from pathlib import Path

from parsers.access_parser import AccessBankParser


class DocumentDetector:

    def process(self, file_path):

        suffix = Path(file_path).suffix.lower()

        if suffix == ".pdf":

            parser = AccessBankParser()

            return parser.extract_transactions(file_path)

        raise ValueError(
            f"Unsupported file type: {suffix}"
        )