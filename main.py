from pathlib import Path

from app import ElixirFinanceAI


def main():

    app = ElixirFinanceAI()

    samples = Path("samples")

    supported_extensions = {
        ".pdf",
        ".jpg",
        ".jpeg",
        ".png"
    }

    files = sorted(
        f for f in samples.iterdir()
        if f.is_file() and f.suffix.lower() in supported_extensions
    )

    if not files:

        print("No supported files found in the samples folder.")

        return

    for file in files:

        print(f"\nProcessing: {file.name}")

        app.process(file)


if __name__ == "__main__":
    main()