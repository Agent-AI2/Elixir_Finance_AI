from ingestion.row_detector import (
    RowDetector
)

text_blocks = [

    {"y": 10},
    {"y": 12},
    {"y": 15},

    {"y": 40},
    {"y": 42},

    {"y": 80},
    {"y": 85},

    {"y": 120},
    {"y": 122}
]

horizontal_lines = [
    0,
    45,
    90,
    135
]

detector = RowDetector()

result = detector.detect(
    text_blocks=text_blocks,
    horizontal_lines=horizontal_lines,
    expected_rows=5
)

print("\nRow Boundaries:")
print(result["row_boundaries"])

print("\nRow Centers:")
print(result["row_centers"])

print("\nEstimated Rows:")
print(result["estimated_rows"])