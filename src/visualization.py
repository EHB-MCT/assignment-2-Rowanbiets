import matplotlib.pyplot as plt

# Standaardbibliotheken
import os


def plot_trends(data, output_path='plots/sport_trends_comparison.png'):
    """
    Visualiseer trends voor verschillende keywords en sla de grafiek op.

    Parameters:
    - data (DataFrame): Dataset met trends en datums.
    - output_path (str): Pad om de grafiek op te slaan.
    """

    # Controleer of de benodigde kolommen aanwezig zijn
    required_columns = ['date', 'sport', 'running', 'cycling', 'swimming', 'yoga', 'gym']
    missing_columns = [col for col in required_columns if col not in data.columns]

    if missing_columns:
        print(f"Ontbrekende kolommen in data: {missing_columns}")
        return

    try:
        # Grafiek maken
        plt.figure(figsize=(12, 8))
        plt.plot(data['date'], data['sport'], label='Sport Populariteit', color='blue')
        plt.plot(data['date'], data['running'], label='Running', color='red')
        plt.plot(data['date'], data['cycling'], label='Cycling', color='green')
        plt.plot(data['date'], data['swimming'], label='Swimming', color='orange')
        plt.plot(data['date'], data['yoga'], label='Yoga', color='purple')
        plt.plot(data['date'], data['gym'], label='Gym', color='brown')

        # Grafiek instellingen
        plt.xlabel('Datum')
        plt.ylabel('Populariteit')
        plt.title('Vergelijking van Sporttrends')
        plt.legend(loc='best')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Zorg dat de uitvoermap bestaat
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Grafiek opslaan
        plt.savefig(output_path)
        plt.show()
        print(f"Grafiek succesvol opgeslagen als '{output_path}'.")

    except Exception as e:
        print(f"Er is een fout opgetreden bij het maken van de grafiek: {e}")
