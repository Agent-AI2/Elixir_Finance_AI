import pandas as pd


def create_expense_analysis(df):

    expense_df = df[df["Debit"] > 0].copy()

    categories = sorted(expense_df["Subcategory"].unique())

    for category in categories:

        expense_df[category] = expense_df.apply(
            lambda row: row["Debit"]
            if row["Subcategory"] == category
            else 0,
            axis=1
        )

    return expense_df


def create_income_analysis(df):

    income_df = df[df["Credit"] > 0].copy()

    categories = sorted(income_df["Subcategory"].unique())

    for category in categories:

        income_df[category] = income_df.apply(
            lambda row: row["Credit"]
            if row["Subcategory"] == category
            else 0,
            axis=1
        )

    return income_df