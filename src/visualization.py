import matplotlib.pyplot as plt

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
