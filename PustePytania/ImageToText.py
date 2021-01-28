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
    patterns_to_rm = [
        r"\n(.)*(PRAWDA)|\n(.)*(FAŁSZ)",
        r"(  )*",
        r"(\n)*",
        r"()",
        r"(Odznacz mój wybór)",
        r"( )*[oO]*( )*[oO]*( )*$"
    ]

    for pattern in patterns_to_rm:
        result = re.compile(pattern).sub('', result)

    # Zwraca wynik
    return result
