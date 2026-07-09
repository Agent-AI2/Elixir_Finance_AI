class CellExtractor:

    def extract(
        self,
        vertical_lines,
        horizontal_lines
    ):

        cells = []

        if len(vertical_lines) < 2:
            return cells

        if len(horizontal_lines) < 2:
            return cells

        row_number = 1

        for row_index in range(
            len(horizontal_lines) - 1
        ):

            y1 = horizontal_lines[row_index]
            y2 = horizontal_lines[
                row_index + 1
            ]

            column_number = 1

            for column_index in range(
                len(vertical_lines) - 1
            ):

                x1 = vertical_lines[
                    column_index
                ]

                x2 = vertical_lines[
                    column_index + 1
                ]

                cell = {

                    "row":
                        row_number,

                    "column":
                        column_number,

                    "x1":
                        x1,

                    "y1":
                        y1,

                    "x2":
                        x2,

                    "y2":
                        y2,

                    "width":
                        x2 - x1,

                    "height":
                        y2 - y1
                }

                cells.append(
                    cell
                )

                column_number += 1

            row_number += 1

        return cells