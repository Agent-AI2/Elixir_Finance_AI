class RowDetector:

    def detect(
        self,
        text_blocks,
        horizontal_lines=None,
        expected_rows=None,
        tolerance=10
    ):

        # -----------------------------
        # Extract OCR Y positions
        # -----------------------------

        y_positions = sorted([
            int(block.get("y", 0))
            for block in text_blocks
        ])

        # -----------------------------
        # Cluster OCR positions
        # -----------------------------

        row_centers = []

        if y_positions:

            cluster = [y_positions[0]]

            for y in y_positions[1:]:

                if abs(y - cluster[-1]) <= tolerance:
                    cluster.append(y)

                else:
                    row_centers.append(
                        int(sum(cluster) / len(cluster))
                    )

                    cluster = [y]

            row_centers.append(
                int(sum(cluster) / len(cluster))
            )

        # -----------------------------
        # Horizontal boundaries
        # -----------------------------

        row_boundaries = sorted(
            list(
                set(horizontal_lines or [])
            )
        )

        # -----------------------------
        # Estimated rows
        # -----------------------------

        estimated_rows = []

        if len(row_boundaries) >= 2:

            for i in range(
                len(row_boundaries) - 1
            ):

                estimated_rows.append({
                    "row_number": i + 1,
                    "start_y": row_boundaries[i],
                    "end_y": row_boundaries[i + 1]
                })

        # -----------------------------
        # Diagnostics
        # -----------------------------

        if expected_rows:

            print(
                f"\nExpected Rows       : {expected_rows}"
            )

            print(
                f"Detected Boundaries : {len(row_boundaries)}"
            )

            print(
                f"Detected OCR Rows   : {len(row_centers)}"
            )

            print(
                f"Estimated Rows      : {len(estimated_rows)}"
            )

        return {

            "row_boundaries":
                row_boundaries,

            "row_centers":
                row_centers,

            "estimated_rows":
                estimated_rows
        }