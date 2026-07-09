import cv2
import numpy as np
from PIL import Image


class PageRectifier:

    def rectify(self, image):

        # -----------------------------------
        # Convert PIL Image to OpenCV format
        # -----------------------------------

        if isinstance(image, Image.Image):
            image = np.array(image)

        if len(image.shape) == 3:
            gray = cv2.cvtColor(
                image,
                cv2.COLOR_RGB2GRAY
            )
        else:
            gray = image.copy()

        # -----------------------------------
        # Threshold image
        # -----------------------------------

        thresh = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY_INV +
            cv2.THRESH_OTSU
        )[1]

        # -----------------------------------
        # Determine skew angle
        # -----------------------------------

        coords = np.column_stack(
            np.where(thresh > 0)
        )

        angle = cv2.minAreaRect(
            coords
        )[-1]

        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle

        # -----------------------------------
        # Rotate image
        # -----------------------------------

        (h, w) = gray.shape[:2]

        center = (
            w // 2,
            h // 2
        )

        matrix = cv2.getRotationMatrix2D(
            center,
            angle,
            1.0
        )

        rectified = cv2.warpAffine(
            image,
            matrix,
            (w, h),
            flags=cv2.INTER_CUBIC,
            borderMode=cv2.BORDER_REPLICATE
        )

        return rectified, angle