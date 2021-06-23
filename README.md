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
Należy utworzyć i skonfigurować bota w [panelu developera](http://discord.com/developers). I skonfigurować zmienną TOKEN w pliku `PustePytania/Config.py`.
Oraz dodać bota do naszego serwera Discord.

Następnie możemy uruchomić bota poleceniem:
```
python3 PustePytania
```

Resztę obsługi wykonujemy na konkretnym kanale na Discordzie, za pomocą odpowiednich poleceń ([Lista poleceń](#lista-poleceń)).


## Lista poleceń
| Polecenie       | Opis
| :-              | :-
| `!readchannel`  | Czyta wszystkie wiadomości na kanale i przetwarza zgodnie z zasadami [Wykorzystanie](#wykorzystanie).
| `!readlast`     | Czyta i przetwarza jedynie wiadomości do pierwszego zdjęcia z reakcją 🆕.
| `!download <ext>` | Pobiera z kanału wszystkie pliki o rozszerzeniu.
| `!filestat <ext>` | Wysyła statystyki, kto ile wrzucił plików o danym formacie.
| `!echo "tekst"` | Odpowiada wiadomością o treści podanej w miejscu `tekst`.


Domyślnie `!readchannel` i `!readlast` zapisują wyniki w folderze `data_files/out`. `!download` zapisuje pliki w `data_files/download`.


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

- Za powtórzenia uznane są screeny, w których liczba różnic w tekście jest większa niż 4 (`Exam.__strictness`).
  Różnica jest wyliczana [Odległością Levenshtein'a](https://pl.wikipedia.org/wiki/Odleg%C5%82o%C5%9B%C4%87_Levenshteina).


## Integracje
### Jak zapisać, jako baza pytań do testownika?
Uruchamiamy w folderze projektu:

```
python3 DoTestownika
```

Domyślnie na podstawie plików z `data_files/out` stworzy bazy testownika dla każdego z testów w folderze `data_files/out_testownik`.

Następnie bazy można połączyć w jedną jedną wspólną bazę poleceniem `./polaczTestowniki.sh` lub wykorzystywać osobno.
```
./polaczTestowniki.sh
```

## Warto doczytać

### Testownik
- Na końcu polecenia w pliku testownika dodawany jest procent na ile odpowiedź jest poprawna;
- Jeżeli pytanie jest uznane za niepewne (odpowiedź "? ? ?") to w pliku testownika, żadna odpowiedź nie jest uznana za poprawną;

### Standardy plików wyjściowych
[Struktura pliku wyjściowego](doc/DOCS.md#Plik-wyjsciowy)

## Autor
Górka Mateusz ([@goorkmateusz](https://goorkamateusz.github.io))

