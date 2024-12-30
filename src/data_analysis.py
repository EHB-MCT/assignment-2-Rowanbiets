import pandas as pd
import matplotlib.pyplot as plt

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

def plot_trends(data):
    """Visualiseer trends voor verschillende keywords."""
    plt.figure(figsize=(12, 8))

    plt.plot(data['date'], data['sport'], label='Sport Populariteit', color='blue')
    plt.plot(data['date'], data['running'], label='Running', color='red')
    plt.plot(data['date'], data['cycling'], label='Cycling', color='green')
    plt.plot(data['date'], data['swimming'], label='Swimming', color='orange')
    plt.plot(data['date'], data['yoga'], label='Yoga', color='purple')
    plt.plot(data['date'], data['gym'], label='Gym', color='brown')

    plt.xlabel('Datum')
    plt.ylabel('Populariteit')
    plt.title('Vergelijking van Sporttrends')
    plt.legend(loc='best')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Opslaan van de grafiek
    plt.savefig('plots/sport_trends_comparison.png')
    plt.show()
    print("Grafiek succesvol opgeslagen als 'sport_trends_comparison.png'.")

def validate_data(data):
    """Controleer de dataset op ontbrekende waarden en vul deze in."""
    print(f"Ontbrekende waarden in de dataset: {data.isnull().sum()}")
    data = data.fillna(method='ffill')  # Vul ontbrekende waarden in met forward fill
    print("Ontbrekende waarden zijn ingevuld.")
    return data

if __name__ == "__main__":
    # Bestanden laden
    cleaned_data = load_data('data/cleaned_data.csv')
    trends_data = load_data('data/trends.csv')

    if cleaned_data is not None and trends_data is not None:
        # Data samenvoegen
        merged_data = merge_data(trends_data, cleaned_data)

        # Data valideren
        validated_data = validate_data(merged_data)

        # Visualisatie
        plot_trends(validated_data)
