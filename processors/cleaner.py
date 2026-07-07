"""
cleaner.py

Contains helper functions for cleaning and standardizing
bank statement data.
"""

import re
from datetime import datetime
import pandas as pd
from processors.categorizer import categorize

def clean_amount(value):
    """
    Converts an amount like:
        '1,500.00' -> 1500.00
        '-'        -> 0.00
        ''         -> 0.00
        None       -> 0.00
    """

    if value is None:
        return 0.0

    value = str(value).strip()

    if value in ("", "-", "None"):
        return 0.0

    value = value.replace(",", "")

    try:
        return float(value)
    except ValueError:
        return 0.0


def clean_date(value):
    """
    Converts:
        13-APR-25

    into a Python datetime object.
    """

    if value is None:
        return None

    value = str(value).strip()

    if value == "":
        return None

    try:
        return datetime.strptime(value, "%d-%b-%y")
    except ValueError:
        return None


def clean_description(value):
    """
    Cleans the transaction narration.
    """

    if value is None:
        return ""

    description = str(value)

    # Remove line breaks
    description = description.replace("\n", " ")

    # Remove extra spaces
    description = re.sub(r"\s+", " ", description)

    return description.strip()


from processors.categorizer import categorize


from processors.categorizer import categorize


def clean_dataframe(df):

    # Clean dates
    df["Posted Date"] = df["Posted Date"].apply(clean_date)
    df["Value Date"] = df["Value Date"].apply(clean_date)

    # Clean amounts
    df["Debit"] = df["Debit"].apply(clean_amount)
    df["Credit"] = df["Credit"].apply(clean_amount)
    df["Balance"] = df["Balance"].apply(clean_amount)

    # Clean descriptions
    df["Description"] = df["Description"].apply(clean_description)

    # Categorize
    results = df["Description"].apply(categorize)

    df["Transaction Type"] = results.apply(
        lambda x: x["Transaction Type"]
    )

    df["Subcategory"] = results.apply(
        lambda x: x["Subcategory"]
    )

    return df