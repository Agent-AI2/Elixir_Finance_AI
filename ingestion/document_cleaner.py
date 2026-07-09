import cv2
import numpy as np
from PIL import Image


class DocumentCleaner:

    def clean(self, image):

        # -----------------------------------
        # Convert PIL image to OpenCV format
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
        # Remove illumination gradients
        # -----------------------------------

        background = cv2.medianBlur(
            gray,
            51
        )

        normalized = cv2.divide(
            gray,
            background,
            scale=255
        )

        # -----------------------------------
        # Improve local contrast
        # -----------------------------------

        clahe = cv2.createCLAHE(
            clipLimit=2.0,
            tileGridSize=(8, 8)
        )

        contrast = clahe.apply(
            normalized
        )

        # -----------------------------------
        # Reduce image noise
        # -----------------------------------

        denoised = cv2.fastNlMeansDenoising(
            contrast,
            None,
            10,
            7,
            21
        )

        # -----------------------------------
        # Adaptive thresholding
        # -----------------------------------

        cleaned = cv2.adaptiveThreshold(
            denoised,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31,
            15
        )

        return cleaned