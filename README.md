# PustePytania
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

## Wykorzystanie
- Wiadomość z zadaniem musi zawierać zdjęcie w formacie jpg lub png.

- Znaczenie reakcji pod wiadomością:
  - Reakcja 🔕 powoduje pominięcie wiadomości;
  - Reakcja 🆕 zapisuje dotychczasowe do pliku i zaczyna zbierać wiadomości do nowego pliku;
  - Reakcje "✔", "✅", "✔️" oznaczają odpowiedź, jako "PRAWDA";
  - Reakcje "❌", "✖" oznaczają odpowiedź, jako "FAŁSZ";
  - Reakcja "⏭" oznacza odpowiedź, jako "NIE WIEM";
  - Pojedyncza reakcja PRAWDA, FAŁSZ oraz NIE WIEM jest pomijana;

- Za powtórzenia uznane są screeny, w których liczba różnic w tekście jest większa niż 4 (`Exam.strictness`).
  Różnica jest wyliczana [Odległością Levenshteina](https://pl.wikipedia.org/wiki/Odleg%C5%82o%C5%9B%C4%87_Levenshteina).

## Autor
Górka Mateusz (@goorkmateusz)

