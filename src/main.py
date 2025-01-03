# Importeer benodigde functies
from data_processing import load_data, merge_data, validate_data
from visualization import plot_trends


def main():
    """
    Voert de hoofdfuncties van het programma uit:
    - Laadt datasets
    - Verwerkt en valideert data
    - Visualiseert trends
    """
    # Bestandspaden definiëren
    cleaned_data_path = 'data/cleaned_data.csv'
    trends_data_path = 'data/trends.csv'

    # Stap 1: Data laden
    print("Stap 1: Data laden...")
    cleaned_data = load_data(cleaned_data_path)
    trends_data = load_data(trends_data_path)

    # Controleer of de data succesvol is geladen
    if cleaned_data is None or trends_data is None:
        print("Kan niet doorgaan. Controleer of beide bestanden correct zijn geladen.")
        return

    # Stap 2: Data samenvoegen
    print("Stap 2: Data samenvoegen...")
    merged_data = merge_data(trends_data, cleaned_data)

    if merged_data.empty:
        print("Kan niet doorgaan. De samengevoegde dataset is leeg.")
        return

    # Stap 3: Data valideren
    print("Stap 3: Data valideren...")
    validated_data = validate_data(merged_data)

    # Stap 4: Visualisatie
    print("Stap 4: Data visualiseren...")
    plot_trends(validated_data)
    print("Visualisatie voltooid!")


# Controleer of dit script direct wordt uitgevoerd
if __name__ == "__main__":
    main()
