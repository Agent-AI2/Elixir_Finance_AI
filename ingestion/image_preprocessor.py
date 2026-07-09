from PIL import Image, ImageOps, ImageFilter
import numpy as np


class ImagePreprocessor:

    def preprocess(self, image):

        # -----------------------------------
        # Convert numpy array to PIL Image
        # -----------------------------------

        if isinstance(
            image,
            np.ndarray
        ):

            image = Image.fromarray(
                image
            )

        # -----------------------------------
        # Convert to grayscale
        # -----------------------------------

        image = ImageOps.grayscale(
            image
        )

        # -----------------------------------
        # Increase contrast
        # -----------------------------------

        image = ImageOps.autocontrast(
            image
        )

        # -----------------------------------
        # Sharpen image
        # -----------------------------------

        image = image.filter(
            ImageFilter.SHARPEN
        )

        return image