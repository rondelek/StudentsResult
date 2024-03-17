import os 
import sys
import dill

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


import numpy as np
import pandas as pd

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

'''
Ta funkcja służy do zapisywania obiektów Pythona do pliku za pomocą modułu `dill`. Oto jej krok po kroku wyjaśnienie:

1. **Argumenty funkcji:**
   - Funkcja `save_object` przyjmuje dwa argumenty:
     - `file_path`: Ścieżka do pliku, w którym chcemy zapisać obiekt.
     - `obj`: Obiekt Pythona, który chcemy zapisać.

2. **Tworzenie katalogu docelowego:**
   - Najpierw funkcja tworzy katalog docelowy, w którym będzie znajdować się plik, jeśli nie istnieje jeszcze. Robi to za pomocą funkcji `os.makedirs`.
   - `os.makedirs(dir_path, exist_ok=True)` tworzy wszystkie katalogi w `dir_path`, jeśli nie istnieją. Parametr `exist_ok=True` oznacza, że funkcja nie wywoła błędu, jeśli katalog już istnieje.

3. **Zapisywanie obiektu do pliku:**
   - Następnie funkcja otwiera plik w trybie binarnym (`'wb'`) za pomocą instrukcji `with open`.
   - Obiekt jest zapisywany do pliku za pomocą funkcji `dill.dump(obj, file_obj)`. Dill jest modułem, który działa podobnie do modułu pickle, ale obsługuje większą różnorodność obiektów Pythona.

4. **Obsługa błędów:**
   - Jeśli wystąpi błąd podczas wykonywania któregokolwiek z powyższych kroków, zostanie wywołany wyjątek. Wyjątek jest przechwytywany przez blok `except`, a następnie jest rzucany niestandardowy wyjątek `CustomException`, który został zdefiniowany gdzie indziej w kodzie.
   - Informacje o błędzie są przekazywane do `CustomException`, aby ułatwić diagnozowanie problemów zapisu obiektu.
'''

def evaluate_models(X_train, y_train,X_test,y_test,models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=5)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)