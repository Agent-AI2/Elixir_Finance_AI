from pathlib import Path

from exporters.excel_exporter import ExcelExporter
from ingestion.document_detector import DocumentDetector
from processors.analysis import (
    create_expense_analysis,
    create_income_analysis,
)


class ElixirFinanceAI:

    def process(self, input_file):

        detector = DocumentDetector()

        df = detector.process(Path(input_file))

        expense = create_expense_analysis(df)

        income = create_income_analysis(df)

        unclassified = df[
            df["Subcategory"] == "Unclassified"
        ]

        exporter = ExcelExporter()

        exporter.export(
            transactions=df,
            expense=expense,
            income=income,
            unclassified=unclassified
        )