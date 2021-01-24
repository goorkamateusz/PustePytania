import pytesseract
from PIL import Image
import re
import requests

def image_to_text( path ):
    """ Konwertuje zdjęcie na tekst """
    # Przetworzenie obrazu
    resp = requests.get( path, stream=True )
    img = Image.open( resp.raw )

    # Analiza obrzu
    result = pytesseract.image_to_string( img, lang="pol" )

    # Przetworzenie tekstu
    result = re.sub( "\n.*(PRAWDA)|\n.*(FAŁSZ)", "", result )
    result = result.replace("\n", " ")
    result = result.replace("  ", " ")
    result = result.replace("  ", " ")
    result = result.replace("", "")
    result = result.replace("Odznacz mój wybór", "")

    # Zwraca wynik
    return result
