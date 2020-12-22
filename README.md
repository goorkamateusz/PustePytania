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

Uruchomić poleceniem:

```
python3 PustePytania.py
```

## Wykorzystanie
- Pomija wiadomości oznaczone: 🔕;
- Reakcja 🆕 włącza zapisywanie do nowego pliku;
- Reakcje "✔", "✅", "✔️" oznaczają odpowiedź "PRAWDA";
- Reakcje "❌", "✖" oznaczają odpowiedź "FAŁSZ";
- Reakcja "⏭" oznacza odpowiedź, jako "nie wiem";