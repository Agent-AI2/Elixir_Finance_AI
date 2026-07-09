class CaptureAssistant:

    def get_profile(self):

        print("\nDetected image-based accounting document.\n")

        print("Select document type:")
        print("1. Analysis Book")
        print("2. Journal")
        print("3. Ledger")
        print("4. Cash Book")
        print("5. Custom")

        choice = input(
            "\nEnter option (1-5): "
        ).strip()

        profiles = {
            "1": "analysis_book",
            "2": "journal",
            "3": "ledger",
            "4": "cash_book",
            "5": "custom"
        }

        profile = profiles.get(
            choice,
            "custom"
        )

        expected_columns = input(
            "\nExpected number of columns (optional): "
        ).strip()

        expected_rows = input(
            "Expected number of rows (optional): "
        ).strip()

        settings = {
            "profile": profile,
            "preview_required": True,
            "expected_columns":
                int(expected_columns)
                if expected_columns
                else None,

            "expected_rows":
                int(expected_rows)
                if expected_rows
                else None
        }

        return settings

    def confirm_preview(self, preview_path):

        print("\nMerged preview created:")
        print(preview_path)

        answer = input(
            "\nDoes the merged preview look correct? (Y/N): "
        ).strip().upper()

        return answer == "Y"

    def get_correction(self):

        print("\nPreview rejected.")

        print("\nChoose correction:")
        print("1. Keep current orientation")
        print("2. Rotate 90° clockwise")
        print("3. Rotate 90° anti-clockwise")
        print("4. Rotate 180°")
        print("5. Change merge direction")
        print("6. Cancel")

        return input(
            "\nSelect option: "
        ).strip()