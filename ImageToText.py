import pytesseract
from PIL import Image
import re
import requests

#
# \brief Konwertuje zdjęcie na tekst
#
def image_to_text( path ):
    # Przetworzenie obrazu
    # img = cv2.imread( path )
    # img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
    # img = cv2.threshold( img, 254, 255, cv2.THRESH_BINARY_INV )[1]
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