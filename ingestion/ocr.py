import cv2
import pytesseract


class OCREngine:

    def extract_text(self, image_path):

        image = cv2.imread(image_path)

        text = pytesseract.image_to_string(image)

        return text