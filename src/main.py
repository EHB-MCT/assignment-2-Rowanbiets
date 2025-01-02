from data_processing import load_data, merge_data, validate_data
from visualization import plot_trends

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
