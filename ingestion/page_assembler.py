from pathlib import Path
import re
from collections import defaultdict


class PageAssembler:
    """
    Groups screenshots that belong to the same physical page.
    """

    PAGE_PATTERN = re.compile(
        r"^(.*?)_page(\d+)(?:_part(\d+))?$",
        re.IGNORECASE
    )

    def assemble(self, image_files):

        pages = defaultdict(list)

        for file in image_files:

            path = Path(file)

            name = path.stem

            match = self.PAGE_PATTERN.match(name)

            if match:

                book_name = match.group(1)

                page = int(match.group(2))

                part = match.group(3)

                if part is None:
                    part = 1
                else:
                    part = int(part)

                pages[(book_name.lower(), page)].append(
                    (part, path)
                )

            else:
                pages[(name.lower(), 1)].append(
                    (1, path)
                )

        assembled_pages = []

        for (_, page), parts in sorted(pages.items()):

            parts.sort(key=lambda x: x[0])

            assembled_pages.append(
                [path for _, path in parts]
            )

        return assembled_pages