# [PL] Token bota
try:
    TOKEN = open("token.txt", 'r').read()
except:
    TOKEN = "twoj token"

# [PL] Nagłówek pliku
FILE_HEAD = "Plik wygenerowany na podstawie ankiet z Discorda"

# [PL] Nazwa pliku wyjściowego
EXAM_NAME = "TestyChronologicznie"

# [PL] Nazwa folderu w którym będzie zapisywać pobrane pliki
DOWNLOAD_DIR = "data_files/download"
