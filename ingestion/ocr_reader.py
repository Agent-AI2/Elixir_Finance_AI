import easyocr
import numpy as np


class OCRReader:

    def __init__(self):

        self.reader = easyocr.Reader(
            ["en"],
            gpu=False
        )

    def read(self, image):

        results = self.reader.readtext(
            np.array(image)
        )

        text_blocks = []

        for box, text, confidence in results:

            xs = [p[0] for p in box]
            ys = [p[1] for p in box]

            text_blocks.append({

                "text": text,

                "x": min(xs),

                "y": min(ys),

                "width": max(xs) - min(xs),

                "height": max(ys) - min(ys),

                "confidence": confidence

            })

        return text_blocks