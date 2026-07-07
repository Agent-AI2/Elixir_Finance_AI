from exporters.excel_exporter import ExcelExporter
from ingestion.import_manager import ImportManager

from processors.analysis import (
    create_expense_analysis,
    create_income_analysis,
)


class ElixirFinanceAI:

    def process(self, input_file):

        import_manager = ImportManager()

        df = import_manager.import_file(input_file)

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