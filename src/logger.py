import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

'''
1. **Tworzenie nazwy pliku dziennika**:
   - Wyobraź sobie, że chcemy napisać historię o tym, co dzieje się w naszej aplikacji. Ta linijka kodu mówi komputerowi, aby wymyślił nazwę dla tej historii. Nazwa powinna zawierać datę i godzinę, abyśmy wiedzieli, kiedy zdarzyły się różne wydarzenia w naszej aplikacji.

2. **Ścieżka do pliku dziennika**:
   - Teraz musimy powiedzieć komputerowi, gdzie chcemy przechowywać tę historię. Ta linijka kodu mówi komputerowi, aby połączył kilka informacji: gdzie teraz jesteśmy (czyli w jakim folderze), nazwę specjalnego folderu, który nazywamy "logs", oraz nazwę historii, którą wymyślił komputer wcześniej. To sprawia, że ​​komputer wie, gdzie ma zapisać naszą historię.

3. **Tworzenie katalogu "logs"**:
   - Czasami potrzebujemy miejsca, gdzie możemy trzymać nasze specjalne historie (logi), aby później łatwo je znaleźć. 
   - Ta linijka kodu mówi komputerowi, aby stworzył specjalny folder, który nazywamy "logs". To tak, jakbyśmy chcieli mieć specjalną szafę, w której możemy trzymać wszystkie nasze historie.

4. **Sprawdzenie, czy folder już istnieje**:
   - Zanim komputer stworzy nowy folder, musi się upewnić, że nie istnieje już taki sam folder. 
   - Ten fragment `exist_ok=True` mówi komputerowi, że jeśli ten folder już istnieje, to wszystko jest w porządku, nie trzeba nic więcej robić. W przeciwnym razie, gdyby ten folder nie istniał, komputer stworzy go dla nas.

   W rezultacie, kiedy nasza aplikacja będzie działać i coś się wydarzy, komputer zapisze tę historię w specjalnym pliku, który będzie przechowywany w folderze "logs". Nazwa tego pliku będzie zawierać datę i czas, abyśmy mogli łatwo znaleźć odpowiednie wydarzenia, gdybyśmy kiedyś potrzebowali sprawdzić, co się wydarzyło.
'''

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s ] %(lineno)d %(name)s — %(levelname)s — %(message)s",
    level = logging.INFO
)

'''
Ta część kodu konfiguruje system logowania (`logging`) w naszej aplikacji. Oto wyjaśnienie każdego elementu:

1. **`logging.basicConfig()`**:
   - Jest to funkcja w module `logging`, która służy do konfigurowania podstawowych ustawień systemu logowania.

2. **`filename = LOG_FILE_PATH`**:
   - Parametr `filename` określa nazwę pliku, do którego będą zapisywane logi. W tym przypadku jest to zmienna `LOG_FILE_PATH`, która zawiera pełną ścieżkę do pliku dziennika.

3. **`format = "[%(asctime)s ] %(lineno)d %(name)s — %(levelname)s — %(message)s"`**:
   - Parametr `format` definiuje format, w jakim będą zapisywane wiadomości logów.
   - `% (asctime) s` wstawia aktualną datę i czas.
   - `% (lineno) d` wstawia numer linii, w której został wywołany log.
   - `% (name) s` wstawia nazwę loggera (jeśli została podana).
   - `% (levelname) s` wstawia poziom logowania (np. INFO, WARNING, ERROR).
   - `% (message) s` wstawia treść samej wiadomości logu.

4. **`level = logging.INFO`**:
   - Parametr `level` określa minimalny poziom logowania, który będzie uwzględniany.
   - W tym przypadku, `logging.INFO` oznacza, że wszystkie wiadomości logów o poziomie INFO lub wyższym (np. WARNING, ERROR) będą uwzględnione.
   - To oznacza, że zostaną zapisane do pliku wszystkie logi o poziomie INFO i wyższym.

W skrócie, ta część kodu mówi systemowi logowania, aby zapisywał wszystkie logi do określonego pliku (`LOG_FILE_PATH`), używając określonego formatu i uwzględniając logi o poziomie INFO i wyższym. Jest to podstawowa konfiguracja systemu logowania, która określa, jak będą wyglądały nasze logi i gdzie zostaną one zapisane.'''

if __name__ == "__main__":
    logging.info("Logging has started")

'''
Ten fragment kodu sprawdza, czy plik został uruchomiony bezpośrednio jako skrypt, czy też został zaimportowany jako moduł do innego pliku. Oto, co oznacza każda linijka:

1. **`if __name__ == "__main__":`**:
   - To jest warunek, który sprawdza, czy wartość specjalnej zmiennej `__name__` jest równa ciągowi `__main__`.
   - `__name__` to zmienna w Pythonie, która zawiera nazwę modułu. Gdy plik jest uruchamiany bezpośrednio, wartość tej zmiennej jest ustawiana na `"__main__"`.
   - W ten sposób ten warunek sprawdza, czy plik został uruchomiony jako główny program.

2. **`logging.info("Logging has started")`**:
   - Jeśli warunek jest spełniony, czyli plik został uruchomiony jako główny program, ta linia kodu zapisuje informację o rozpoczęciu logowania.
   - `logging.info()` to funkcja, która rejestruje wiadomość o poziomie INFO, informującą o tym, że logowanie zostało rozpoczęte.

W skrócie, jeśli ten plik zostanie uruchomiony bezpośrednio (a nie zaimportowany jako moduł), zarejestrowana zostanie wiadomość o poziomie INFO informująca, że logowanie zostało rozpoczęte. Jest to przydatne, abyśmy mogli śledzić, kiedy logowanie zaczyna i kończy się w naszej aplikacji.
'''