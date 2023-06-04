**************************************************
Dokumentacja Programu Rozpoznawania Mowy
**************************************************

Wprowadzenie:
--------------
Ten program wykorzystuje bibliotekę rozpoznawania mowy Vosk wraz z PyAudio i pyttsx3 do przeprowadzania rozpoznawania mowy w czasie rzeczywistym, konwersji tekstu na mowę oraz wykonywania określonych akcji na podstawie rozpoznanej mowy. Program umożliwia interakcję użytkowników z systemem poprzez wypowiadanie poleceń i wykonywanie odpowiednich działań.

Zależności:
--------------
- vosk: Vosk to otwarta biblioteka rozpoznawania mowy, która umożliwia rozpoznawanie mowy offline. Wykorzystywana jest do rozpoznawania mowy w czasie rzeczywistym.
- pyaudio: PyAudio to biblioteka Pythona, która zapewnia interfejs do biblioteki PortAudio do obsługi wejścia i wyjścia audio. Wykorzystywana jest do nagrywania dźwięku z mikrofonu i odtwarzania dźwięku.
- pyttsx3: pyttsx3 to biblioteka Pythona, która zapewnia interfejs do konwersji tekstu na mowę. Wykorzystywana jest do przekształcania rozpoznanego tekstu na wypowiedź mówioną.
- webbrowser: webbrowser to wbudowany moduł Pythona, który zapewnia wysokopoziomowe interfejsy do otwierania przeglądarek internetowych. Wykorzystywany jest do przeprowadzania wyszukiwań w sieci na podstawie rozpoznanej mowy.
- requests: requests to biblioteka Pythona, która zapewnia możliwość wysyłania zapytań HTTP. Wykorzystywana jest do wysyłania danych z programu do serwera webowego.

Sposób użycia:
--------------
1. Upewnij się, że wymagane zależności są zainstalowane.
2. Pobierz model Vosk dla wybranego języka i podaj ścieżkę do modelu w kodzie.
3. Uruchom program.
4. Wypowiadaj polecenia lub wprowadzaj mowę jako wejście dla programu.

Funkcje:
--------------
1. Rozpoznawanie Mowy w Czasie Rzeczywistym: Program wykorzystuje bibliotekę Vosk do rozpoznawania mowy w czasie rzeczywistym z wejścia mikrofonu.
2. Konwersja Tekstu na Mowę: Program wykorzystuje bibliotekę pyttsx3 do przekształcania rozpoznanego tekstu na mowę.
3. Wykonywanie Poleceń: Definiowanie konkretnych poleceń i wykonywanie odpowiednich akcji na podstawie rozpoznanej mowy.
4. Wyszukiwanie w Google: Przeprowadzanie wyszukiwania w sieci na podstawie rozpoznanej mowy zaczynającej się od słowa kluczowego "znajdź".
5. Zapis Mowy do Pliku: Zapisywanie rozpoznanej mowy do pliku, jeśli rozpoczyna się ona od słowa kluczowego "zapisz".
6. Odczytywanie Plików: Odczytywanie tekstu z pliku, jeśli rozpoznana mowa rozpoczyna się od słowa kluczowego "odczytaj".
7. Wsparcie dla wielu języków: Ustawianie preferowanego języka dla rozpoznawania mowy i konwersji tekstu na mowę.

Dodatkowe funkcje:
--------------
- Wysyłanie rozpoznanego tekstu do serwera internetowego: Program może wysłać rozpoznany tekst do serwera internetowego hostowanego na localhost za pomocą protokołu HTTP.
- Wyświetlanie rozpoznanego tekstu w tabeli trzech kolumn: Program dostarcza prosty interfejs internetowy, który wyświetla otrzymany rozpoznany tekst w układzie tabeli trzech kolumn.

Ważne uwagi:
--------------
- Upewnij się, że podmieniłeś ścieżkę modelu Vosk na prawidłową ścieżkę na swoim systemie.
- Upewnij się, że nadano niezbędne uprawnienia dostępu do mikrofonu oraz zapisu plików na systemie.

