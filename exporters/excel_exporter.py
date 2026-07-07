import pandas as pd


class ExcelExporter:

    def export(
        self,
        transactions,
        expense,
        income,
        unclassified,
        output_file="outputs/Elixir_Finance_Report.xlsx"
    ):

        with pd.ExcelWriter(
            output_file,
            engine="openpyxl"
        ) as writer:

            transactions.to_excel(
                writer,
                sheet_name="Transactions",
                index=False
            )

            expense.to_excel(
                writer,
                sheet_name="Expense Analysis",
                index=False
            )

            income.to_excel(
                writer,
                sheet_name="Income Analysis",
                index=False
            )

            unclassified.to_excel(
                writer,
                sheet_name="Unclassified Transactions",
                index=False
            )

        print(f"\nReport generated successfully: {output_file}")