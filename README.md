# PustePytania
Bot Discorda przetwarzający zrzuty ekranu pytań tworzy plik z odpowiedziami.

## Instalacja
- Należy zainstalować oprogramowanie `Tesseract-OCR` od Google,
  razem z pakietem obsługującym język polski.
```
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-pol
```

- Wymaga paczek:
```
pip install pytesseract
pip install discord.py
pip install requests
pip install re
```

## Uruchomienie
Należy utworzyć i skonfigurować bota. I skonfigurować zmienną TOKEN w pliku PrivateData.py.

## Wykorzystanie
- Pomija wiadomości oznaczone: 🔕;
- Reakcja 🆕 włącza zapisywanie do nowego pliku;
- Reakcje "❌", "✖" oznaczają FAŁSZ;
- Reakcje "✔", "✅", "✔️" oznaczają PRAWDA;