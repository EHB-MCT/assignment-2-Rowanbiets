# Standaardbibliotheken
import os

# Externe bibliotheken
import pandas as pd


def load_data(file_path: str) -> pd.DataFrame | None:
    """
    Laad data vanuit een CSV-bestand.

    Args:
        file_path (str): Het pad naar het CSV-bestand.

    Returns:
        pd.DataFrame | None: De geladen dataset of None als er een fout optreedt.
    """
    if not os.path.exists(file_path):
        print(f"Bestand {file_path} niet gevonden.")
        return None

    try:
        data = pd.read_csv(file_path)
        if data.empty:
            print(f"Bestand {file_path} is leeg.")
            return None
        print(f"Data succesvol geladen vanuit {file_path}.")
        return data
    except pd.errors.ParserError:
        print(f"Fout bij het verwerken van {file_path}. Controleer de inhoud van het bestand.")
    except Exception as e:
        print(f"Er is een onverwachte fout opgetreden: {e}")
    return None


def merge_data(trends_data: pd.DataFrame, cleaned_data: pd.DataFrame) -> pd.DataFrame:
    """
    Merge trends data met de schone data op basis van de 'date' kolom.

    Args:
        trends_data (pd.DataFrame): Dataset met trendgegevens.
        cleaned_data (pd.DataFrame): Schoongemaakte dataset.

    Returns:
        pd.DataFrame: De samengevoegde dataset.
    """
    try:
        # Converteer datums naar datetime-indeling
        trends_data['date'] = pd.to_datetime(trends_data['date'], errors='coerce')
        cleaned_data['date'] = pd.to_datetime(cleaned_data['date'], errors='coerce')

        # Controleer op ontbrekende datums
        if trends_data['date'].isnull().any() or cleaned_data['date'].isnull().any():
            print("Waarschuwing: Sommige datums zijn ongeldig en worden overgeslagen.")

        # Merge datasets
        merged_data = pd.merge(trends_data, cleaned_data, on='date', how='left')
        print("Data succesvol samengevoegd.")
        return merged_data

    except KeyError:
        print("Kolom 'date' ontbreekt in een van de datasets.")
        return pd.DataFrame()  # Lege dataframe teruggeven bij fout
    except Exception as e:
        print(f"Er is een fout opgetreden tijdens het samenvoegen van data: {e}")
        return pd.DataFrame()


def validate_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Controleer de dataset op ontbrekende waarden en vul deze in.

    Args:
        data (pd.DataFrame): De dataset om te valideren.

    Returns:
        pd.DataFrame: De gevalideerde dataset.
    """
    try:
        missing_values = data.isnull().sum()
        print(f"Ontbrekende waarden per kolom:\n{missing_values}")

        # Vul ontbrekende waarden in met forward fill
        validated_data = data.fillna(method='ffill')
        print("Ontbrekende waarden zijn ingevuld (forward fill).")
        return validated_data

    except Exception as e:
        print(f"Fout bij het valideren van data: {e}")
        return data  # Retourneer ongewijzigde data bij fout
