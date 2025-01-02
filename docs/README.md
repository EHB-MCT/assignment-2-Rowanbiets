# Sports Activity Data Project

## Project Overview
This project collects, analyzes, and visualizes sports activity data using public data sources such as Google Trends. The goal is to uncover trends, provide insights, and make data-driven decisions based on sports activity popularity.

## Folder Structure
```
├── data/
│   ├── trends.csv                # Raw data collected from Google Trends
│   ├── cleaned_data.csv          # Processed and cleaned dataset
│   └── merged_data.csv           # Final merged dataset used for visualization
├── docs/
│   ├── README.md                 # Overview and setup instructions (this file)
│   ├── dataflow.md               # Data flow documentation with diagrams
│   ├── decisions.md              # Design decisions and assumptions
│   └── design_patterns.md        # Explanation of design patterns used
├── plots/
│   └── sport_trends_comparison.png # Visualization output
├── src/
│   ├── data_processing.py        # Script for processing and validating data
│   ├── visualization.py          # Script for visualizing data
│   └── main.py                   # Main script to run the application
├── .gitignore                    # Files and directories to be ignored by Git
├── requirements.txt              # Required Python packages
└── LICENSE                       # Open-source license for the project
```

## Getting Started

### Prerequisites
- Python 3.8 or later
- `pip` (Python package manager)
- Internet connection (for fetching Google Trends data)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Run the data collection script to fetch data:
   ```bash
   python src/data_collection.py
   ```
2. Process and validate the data:
   ```bash
   python src/data_processing.py
   ```
3. Visualize the data trends:
   ```bash
   python src/visualization.py
   ```
4. Alternatively, run the main script to execute all steps:
   ```bash
   python src/main.py
   ```

## Contributing
Feel free to contribute by creating issues, submitting pull requests, or suggesting new features. Please follow the branching and commit conventions described below.

### Git Workflow
- **`main`**: Contains the stable version of the project.
- **`develop`**: Main development branch.
- **`feature/data-collection`**: Branch for new features.

### Commit Message Conventions
Follow the [Conventional Commits](https://www.conventionalcommits.org/) standard:
- `feat`: Introduces a new feature.
- `fix`: Fixes a bug.
- `chore`: Updates to configuration files, documentation, or other non-code elements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
- Rowan Biets

---
