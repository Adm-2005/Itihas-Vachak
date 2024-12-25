import os
import pymupdf
import pytesseract
from PIL import Image
from io import BytesIO

pytesseract.tesseract_cmd = "/usr/bin/tesseract"

class PdfExtractor:
    def __init__(self, pdf_path: str, is_scanned: bool):
        self.pdf_path = pdf_path
        self.is_scanned = is_scanned
        self.book = pymupdf.open(self.pdf_path)

    def extract_from_image(self, page):
        pix = page.get_pixmap()
        img_data = pix.tobytes()
        img = Image.open(BytesIO(img_data))

        text = pytesseract.image_to_string(img)
        return text

    def extract_text(self):
        text = ''
        for page_idx in range(len(self.book)):
            page = self.book.load_page(page_idx)
            
            if self.is_scanned:
                text += self.extract_from_image(page)
            else:
                text += page.get_text()

        return text