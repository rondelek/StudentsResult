import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifact', 'train.csv')
    test_data_path: str=os.path.join('artifact', 'test.csv')
    raw_data_path: str=os.path.join('artifact', 'raw.csv')



'''
Ta klasa jest jak opakowanie dla informacji dotyczącej ścieżek plików, które będą używane do wczytywania danych. Przechowuje informacje o trzech rodzajach plików: plikach treningowych, testowych i surowych. W ten sposób, gdy tworzysz instancję tej klasy, możesz zdefiniować, gdzie znajdują się te pliki.

Na przykład:

config = DataIngestionConfig()

Tworzy obiekt `config` klasy `DataIngestionConfig` z domyślnymi ścieżkami do plików (czyli 'artifact/train.csv', 'artifact/test.csv' i 'artifact/raw.csv').

Jeśli chcesz użyć innych plików, możesz to zrobić tak:


config = DataIngestionConfig(train_data_path='moje_dane/train.csv', test_data_path='moje_dane/test.csv', raw_data_path='moje_dane/raw.csv')

Wtedy `config` będzie zawierać twoje niestandardowe ścieżki do plików. To wszystko! Ta klasa po prostu przechowuje informacje o ścieżkach plików i pozwala na łatwe dostosowywanie tych ścieżek.
'''
'''
`DataIngestionConfig` może być użyte w sytuacjach, gdy masz aplikację lub skrypt, który potrzebuje informacji o ścieżkach do plików danych. Oto kilka przykładów, kiedy mogą być przydatne:

1. Wczytywanie danych do analizy:
   - Jeśli tworzysz aplikację lub skrypt do analizy danych, `DataIngestionConfig` może przechowywać informacje o ścieżkach do plików z danymi treningowymi, testowymi i surowymi. To ułatwia wczytywanie tych danych do analizy.

2. Trenowanie modeli uczenia maszynowego:
   - Podczas trenowania modeli uczenia maszynowego, często musisz wczytać dane treningowe i testowe z odpowiednich plików. `DataIngestionConfig` może przechowywać informacje o tych ścieżkach, ułatwiając dostęp do danych treningowych i testowych dla różnych modeli.

3. Testowanie modeli:
   - Podobnie jak w przypadku trenowania modeli, podczas testowania modeli uczenia maszynowego przydatne jest wczytywanie danych testowych z odpowiednich plików. `DataIngestionConfig` może pomóc w zarządzaniu ścieżkami do tych danych.

4. Skrypty automatyzujące przetwarzanie danych:
   - Jeśli masz skrypt, który automatyzuje przetwarzanie danych, `DataIngestionConfig` może przechowywać informacje o ścieżkach do plików, które są przetwarzane. Na przykład, jeśli codziennie otrzymujesz nowe pliki danych, `DataIngestionConfig` może pomóc w łatwym dostępie do tych plików.

Ogólnie rzecz biorąc, `DataIngestionConfig` jest używane wszędzie tam, gdzie potrzebujesz trzymać informacje o ścieżkach plików danych i chcesz, aby były one łatwo dostępne i konfigurowalne.
'''

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of the data is completed')

            return (
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
        

'''
Kiedy tworzymy nową rzecz, chcemy jej dać pewne ustawienia, prawda? Na przykład, kiedy dostajesz nowy komputer do zabawy, musisz go skonfigurować - ustawić hasło, tapetę, itp. W kodzie jest podobnie!

Klasa `DataIngestion` to jak komputer, który potrafi wczytywać dane. Ale musi wiedzieć, gdzie są te dane, prawda? Tutaj wchodzi na scenę `DataIngestionConfig`. To taki zeszyt z ustawieniami, w którym mówisz komputerowi, gdzie znajdują się pliki z danymi.

W linii `def __init__(self):`, mówimy komputerowi (czyli Pythonowi), że kiedy będziemy tworzyć nowy komputer (czyli obiekt klasy `DataIngestion`), chcemy, żeby od razu miał ten zeszyt z ustawieniami (`DataIngestionConfig`). Tak więc, ta linia kodu mówi Pythonowi: "Stwórz zeszyt z ustawieniami dla tego komputera".

A linia `self.ingestion_config = DataIngestionConfig()` to jak włożenie tego zeszytu z ustawieniami do komputera. Teraz komputer będzie mógł korzystać z tych ustawień, kiedy będzie potrzebował wczytywać dane.
'''

if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()