from pathlib import Path

from app import ElixirFinanceAI


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png"
}


def main():

    app = ElixirFinanceAI()

    sample_folder = Path("samples")

    files = sorted(
        f for f in sample_folder.iterdir()
        if f.is_file()
        and f.suffix.lower() in SUPPORTED_EXTENSIONS
    )

    processed_image_batch = False

    for file in files:

        suffix = file.suffix.lower()

        # ---------------------------------
        # Process PDFs individually
        # ---------------------------------

        if suffix == ".pdf":

            print(
                f"\nProcessing: {file.name}"
            )

            app.process(file)

        # ---------------------------------
        # Process all images as one batch
        # ---------------------------------

        elif suffix in {
            ".jpg",
            ".jpeg",
            ".png"
        }:

            if processed_image_batch:
                continue

            print(
                "\nProcessing account book images..."
            )

            app.process(file)

            processed_image_batch = True


if __name__ == "__main__":
    main()