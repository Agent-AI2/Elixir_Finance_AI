from pathlib import Path

from ingestion.document_detector import DocumentDetector


class ImportManager:

    def import_file(self, input_file):

        detector = DocumentDetector()

        dataframe = detector.process(Path(input_file))

        return dataframe