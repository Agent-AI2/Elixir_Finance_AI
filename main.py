from app import ElixirFinanceAI


def main():

    app = ElixirFinanceAI()

    app.process(
        "samples/access_statement.pdf"
    )


if __name__ == "__main__":
    main()