from ingestion.book_builder import BookBuilder

builder = BookBuilder()

draft = builder.build([
    "samples/account_book.jpg"
])

print("\nDraft Book\n")
print(f"Source Files : {draft['source_files']}")
print(f"Width        : {draft['image_width']}")
print(f"Height       : {draft['image_height']}")
print(f"Status       : {draft['status']}")
print(f"Columns      : {draft['columns']}")
print(f"Rows         : {draft['rows']}")