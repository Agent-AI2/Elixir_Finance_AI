from parsers.access_parser import AccessBankParser


def main():

    parser = AccessBankParser()

    df = parser.extract_transactions(
        "samples/access_statement.pdf"
    )

    print(df.info())

    print(df.head(10))

    df.to_excel(
        "outputs/access_transactions.xlsx",
        index=False
    )

    print("\n✅ Excel exported successfully!")


if __name__ == "__main__":
    main()