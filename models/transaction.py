from dataclasses import dataclass


@dataclass
class Transaction:

    posted_date: str = ""
    value_date: str = ""

    description: str = ""

    debit: float = 0.0
    credit: float = 0.0
    balance: float = 0.0

    account_name: str = ""
    account_number: str = ""

    source: str = ""
    source_type: str = ""

    transaction_type: str = ""
    subcategory: str = ""