from ingestion.cell_extractor import (
    CellExtractor
)

vertical_lines = [
    0,
    100,
    300,
    500,
    700
]

horizontal_lines = [
    0,
    50,
    100,
    150
]

extractor = (
    CellExtractor()
)

cells = (
    extractor.extract(
        vertical_lines,
        horizontal_lines
    )
)

print(
    f"\nDetected "
    f"{len(cells)} cells.\n"
)

for cell in cells:

    print(cell)