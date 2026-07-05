from abc import ABC, abstractmethod
import pandas as pd


class BaseParser(ABC):
    """
    Base class for all bank statement parsers.
    Every bank parser must inherit from this class.
    """

    @abstractmethod
    def extract_account_info(self, pdf_path: str) -> dict:
        """Extract account details from the statement."""
        pass

    @abstractmethod
    def extract_transactions(self, pdf_path: str) -> pd.DataFrame:
        """Extract all transactions from the statement."""
        pass