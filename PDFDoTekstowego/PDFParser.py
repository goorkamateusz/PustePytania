import pdftotext
import os

class PDFParser:

    @staticmethod
    def get_text_from_pdf(file_path: str) -> str:
        """ public """
        text = ""
        with open(file_path, "rb") as file:
            pdf = pdftotext.PDF(file)
            text = "\n\n".join( pdf )
        return text

    @staticmethod
    def is_pdf(file_path: str) -> str:
        """ public """
        if not os.path.isfile(file_path):
            return False
        if file_path.split(".")[-1] != "pdf":
            return False
        return True
