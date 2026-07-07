from pathlib import Path
import pandas as pd

from ingestion.document_detector import DocumentDetector
from exporters.excel_exporter import ExcelExporter
from processors.analysis import (
    create_expense_analysis,
    create_income_analysis,
)


class ElixirFinanceAI:

    def process(self, input_file):

        detector = DocumentDetector()

        result = detector.process(Path(input_file))

        # ==========================================
        # ACCOUNT BOOK WORKFLOW
        # ==========================================
        if isinstance(result, list):

            print("\nDraft Digital Account Book Created\n")

            for page in result:

                print(f"Page Number : {page['page_number']}")
                print(f"Source Files: {page['source_files']}")
                print(
                    f"Image Size  : "
                    f"{page['image_width']} x {page['image_height']}"
                )
                print(f"Status      : {page['status']}")
                print("-" * 50)

            return result

        # ==========================================
        # BANK STATEMENT WORKFLOW
        # ==========================================
        elif isinstance(result, pd.DataFrame):

            df = result

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

            return df

        # ==========================================
        # UNKNOWN OBJECT
        # ==========================================
        else:

            raise TypeError(
                "Unsupported object returned by DocumentDetector."
            )