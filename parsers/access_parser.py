"""
Access Bank Statement Parser
"""

import pdfplumber
import pandas as pd

from .base_parser import BaseParser
from processors.validator import is_transaction
from processors.cleaner import (
    clean_dataframe,
    clean_description,
)


class AccessBankParser(BaseParser):
    """
    Parser for Access Bank PDF statements.
    """

    def extract_account_info(self, pdf_path: str):
        """
        Placeholder for extracting account details.
        This will be implemented later.
        """
        return {}

    def extract_transactions(self, pdf_path: str) -> pd.DataFrame:
        """
        Extracts all transactions from an Access Bank statement.
        """

        transactions = []

        with pdfplumber.open(pdf_path) as pdf:

            print(f"\nProcessing {len(pdf.pages)} pages...\n")

            for page_number, page in enumerate(pdf.pages, start=1):

                print(f"Reading Page {page_number}")

                tables = page.extract_tables()

                if not tables:
                    continue

                for table in tables:

                    if not table:
                        continue

                    for row in table:

                        # Ignore rows that are not transactions
                        if not is_transaction(row):
                            continue

                        # Ensure we always have 6 columns
                        while len(row) < 6:
                            row.append("")

                        transaction = {
                            "Posted Date": row[0],
                            "Value Date": row[1],
                            "Description": clean_description(row[2]),
                            "Debit": row[3],
                            "Credit": row[4],
                            "Balance": row[5],
                        }

                        transactions.append(transaction)

        df = pd.DataFrame(transactions)

        # Clean the dataframe
        df = clean_dataframe(df)

        print(f"\n{len(df)} transactions extracted successfully.\n")

        return df