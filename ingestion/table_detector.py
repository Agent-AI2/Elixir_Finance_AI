import cv2
import numpy as np
from PIL import Image


class TableDetector:

    def __init__(
        self,
        vertical_kernel_height=80,
        horizontal_kernel_width=120,
        vertical_threshold_ratio=0.35,
        horizontal_threshold_ratio=0.30,
        vertical_tolerance=25,
        horizontal_tolerance=15
    ):

        self.vertical_kernel_height = (
            vertical_kernel_height
        )

        self.horizontal_kernel_width = (
            horizontal_kernel_width
        )

        self.vertical_threshold_ratio = (
            vertical_threshold_ratio
        )

        self.horizontal_threshold_ratio = (
            horizontal_threshold_ratio
        )

        self.vertical_tolerance = (
            vertical_tolerance
        )

        self.horizontal_tolerance = (
            horizontal_tolerance
        )

    def detect(self, image):

        # -----------------------------
        # Convert PIL to numpy
        # -----------------------------

        if isinstance(image, Image.Image):
            image = np.array(image)

        # -----------------------------
        # Convert to grayscale
        # -----------------------------

        if len(image.shape) == 3:

            gray = cv2.cvtColor(
                image,
                cv2.COLOR_BGR2GRAY
            )

        else:

            gray = image

        # -----------------------------
        # Binary inversion
        # -----------------------------

        binary = cv2.threshold(
            gray,
            180,
            255,
            cv2.THRESH_BINARY_INV
        )[1]

        # -----------------------------
        # Vertical line detection
        # -----------------------------

        vertical_kernel = (
            cv2.getStructuringElement(
                cv2.MORPH_RECT,
                (
                    1,
                    self.vertical_kernel_height
                )
            )
        )

        vertical_image = (
            cv2.morphologyEx(
                binary,
                cv2.MORPH_OPEN,
                vertical_kernel,
                iterations=2
            )
        )

        # -----------------------------
        # Horizontal line detection
        # -----------------------------

        horizontal_kernel = (
            cv2.getStructuringElement(
                cv2.MORPH_RECT,
                (
                    self.horizontal_kernel_width,
                    1
                )
            )
        )

        horizontal_image = (
            cv2.morphologyEx(
                binary,
                cv2.MORPH_OPEN,
                horizontal_kernel,
                iterations=2
            )
        )

        # -----------------------------
        # Extract line positions
        # -----------------------------

        vertical_positions = (
            self._extract_positions(
                vertical_image,
                axis=0,
                threshold_ratio=
                self.vertical_threshold_ratio
            )
        )

        horizontal_positions = (
            self._extract_positions(
                horizontal_image,
                axis=1,
                threshold_ratio=
                self.horizontal_threshold_ratio
            )
        )

        # -----------------------------
        # Compress duplicates
        # -----------------------------

        vertical_positions = (
            self._compress(
                vertical_positions,
                tolerance=
                self.vertical_tolerance
            )
        )

        horizontal_positions = (
            self._compress(
                horizontal_positions,
                tolerance=
                self.horizontal_tolerance
            )
        )

        return {

            "vertical_lines":
                vertical_positions,

            "horizontal_lines":
                horizontal_positions,

            "vertical_image":
                vertical_image,

            "horizontal_image":
                horizontal_image
        }

    def _extract_positions(
        self,
        image,
        axis,
        threshold_ratio
    ):

        positions = []

        projection = np.sum(
            image,
            axis=axis
        )

        threshold = (
            projection.max() *
            threshold_ratio
        )

        for index, value in enumerate(
            projection
        ):

            if value > threshold:
                positions.append(
                    index
                )

        return positions

    def _compress(
        self,
        positions,
        tolerance
    ):

        if not positions:
            return []

        compressed = [
            positions[0]
        ]

        for pos in positions[1:]:

            if (
                pos -
                compressed[-1]
            ) > tolerance:

                compressed.append(
                    pos
                )

        return compressed