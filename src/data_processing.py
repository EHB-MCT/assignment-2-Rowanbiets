import pandas as pd
import os

def load_data(file_path):
    """Laad data vanuit een CSV-bestand."""
    try:
        data = pd.read_csv(file_path)
        print(f"Data succesvol geladen vanuit {file_path}.")
        return data
    except FileNotFoundError:
        print(f"Bestand {file_path} niet gevonden.")
    except pd.errors.EmptyDataError:
        print(f"Bestand {file_path} is leeg.")
    return None

def merge_data(trends_data, cleaned_data):
    """Merge trends data met de schone data op basis van de 'date' kolom."""
    cleaned_data['date'] = pd.to_datetime(cleaned_data['date'])
    trends_data['date'] = pd.to_datetime(trends_data['date'])
    merged_data = pd.merge(trends_data, cleaned_data, on='date', how='left')
    print("Data succesvol samengevoegd.")
    return merged_data

def validate_data(data):
    """Controleer de dataset op ontbrekende waarden en vul deze in."""
    print(f"Ontbrekende waarden in de dataset: {data.isnull().sum()}")
    data = data.fillna(method='ffill')  # Vul ontbrekende waarden in met forward fill
    print("Ontbrekende waarden zijn ingevuld.")
    return data
