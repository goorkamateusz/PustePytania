# PustePytania (pakiet)

## Spis treści
- [PustePytania (pakiet)](#pustepytania-pakiet)
  - [Spis treści](#spis-treści)
  - [Autor](#autor)
- [PustePytania (bot)](#pustepytania-bot)
  - [Instalacja](#instalacja)
  - [Uruchomienie](#uruchomienie)
    - [Jak zapisać, jako baza pytań do testownika?](#jak-zapisać-jako-baza-pytań-do-testownika)
  - [Wykorzystanie](#wykorzystanie)
  - [Warto doczytać](#warto-doczytać)
    - [Testownik](#testownik)
    - [Standardy plików wyjściowych](#standardy-plików-wyjściowych)
- [PDFDoTekstowego](#pdfdotekstowego)
  - [Instalacja](#instalacja-1)
  - [Uruchomienie](#uruchomienie-1)
- [DoTestownika](#dotestownika)

## Autor
Górka Mateusz (@goorkmateusz)



___
<br/><br/>

# PustePytania (bot)
Bot na Discorda przetwarzający zrzuty ekranu pytań i tworzy plik ze zbiorem odpowiedzi.

## Instalacja
- Bot testowany jedynie na systemie Linux.

- Należy zainstalować oprogramowanie `Tesseract-OCR` od Google, razem z pakietem obsługującym język polski.
```
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-pol
```

- Instalacja modułów:
```
pip3 install -r requirements.txt
```

## Uruchomienie
Należy utworzyć i skonfigurować bota w [panelu developera](http://discord.com/developers).
I skonfigurować zmienną TOKEN w pliku `Config.py`.

Następnie uruchamiamy poleceniem:
```
python3 PustePytania
```

Domyślnie w folderze `out` zapiszą się pliki z testami!

### Jak zapisać, jako baza pytań do testownika?
Uruchamiamy w folderze bota:

```
python3 DoTestownika
```

Domyślnie w folderze `out_testownik` zapiszą się bazy pytań do każdego z testu.

Możesz je wykorzystywać osobno, albo połączyć w jedną wspólną bazę poleceniem:

```
./polaczTestowniki.sh
```

## Wykorzystanie
- Wiadomość z zadaniem musi zawierać zdjęcie w formacie jpg lub png.

- Znaczenie reakcji pod wiadomością:
  - Reakcja 🔕 powoduje pominięcie wiadomości;
  - Reakcja 🛑 powoduje, że wszystkie wiadomości do wiadomości
    z reakcją 🆕 są pomijane (ta wiadomość jest już brana pod uwagę);
  - Reakcja 🆕 zapisuje dotychczasowe do pliku i zaczyna zbierać wiadomości do nowego pliku;
  - Reakcje "✔", "✅", "✔️" oznaczają odpowiedź, jako `PRAWDA`;
  - Reakcje "❌", "✖" oznaczają odpowiedź, jako `FAŁSZ`;
  - Reakcja "⏭" oznacza odpowiedź, jako `NIE WIEM`;
  - Pojedyncza reakcja `PRAWDA`, `FAŁSZ` oraz `NIE WIEM` jest pomijana;

- Za powtórzenia uznane są screeny, w których liczba różnic w tekście jest większa niż 4 (`Exam.strictness`).
  Różnica jest wyliczana [Odległością Levenshteina](https://pl.wikipedia.org/wiki/Odleg%C5%82o%C5%9B%C4%87_Levenshteina).


## Warto doczytać

### Testownik
- Na końcu polecenia w pliku testownika dodawany jest procent na ile odpowiedź jest poprawna;
- Jeżeli pytanie jest uznane za niepewne (odpowiedź "? ? ?") to w pliku testownika, żadna odpowiedź nie jest poprawna;

### Standardy plików wyjściowych
[Struktura pliku wyjściowego](DOCS.md#Plik-wyjsciowy)



___
<br/><br/>

# PDFDoTekstowego
Przetwarza wiele plików PDF do listy zadań usuwając powtórzone zadania.

## Instalacja
Wymaga zainstalowania modułów: `pdftotext`, `re`

## Uruchomienie
```
python3 PDFDoTekstowego
```



___
<br/><br/>

# DoTestownika
Zobacz jak wykorzystać razem z [botem PustePytania](#jak-zapisać-jako-baza-pytań-do-testownika).
