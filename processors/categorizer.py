import json
from pathlib import Path

RULE_FILE = Path("rules/categories.json")

with open(RULE_FILE, "r", encoding="utf-8") as f:
    RULES = json.load(f)["rules"]


def categorize(description):

    if description is None:
        description = ""

    description = description.upper()

    for rule in RULES:

        for keyword in rule["keywords"]:

            if keyword.upper() in description:

                return {
                    "Transaction Type": rule["transaction_type"],
                    "Subcategory": rule["subcategory"]
                }

    return {
        "Transaction Type": "Unknown",
        "Subcategory": "Unclassified"
    }