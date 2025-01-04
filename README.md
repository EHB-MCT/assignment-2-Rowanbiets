# Sports Activity Data Project

## Project Overview
This project aims to collect, analyze, and document data about sports activities using public data sources. The data will be processed and visualized to uncover trends and provide insights into popular sports activities over time.

## Goal
The main objective of this project is to analyze trends in sports activities and provide visual insights into their popularity. This information can be used by researchers, fitness enthusiasts, and marketers to better understand trends and plan strategies accordingly.

## Folder Structure
```
├── data/
│   ├── trends.csv                # Raw data collected from Google Trends
│   └── cleaned_data.csv          # Processed and cleaned dataset
├── docs/
│   ├── README.md                 # Overview and setup instructions (this file)
│   ├── process.md                # Documentation of data processing steps
│   ├── changelog.md              # Record of changes and updates
│   ├── code_of_conduct.md        # Code of conduct for contributors
│   └── contributing.md           # Guidelines for contributing to the project
├── src/
│   ├── data_processing.py        # Script for data processing
│   ├── main.py                   # Main script for executing the project
│   └── visualization.py          # Script for visualizing data
├── plots/                        # Folder for storing generated plots
├── requirements.txt              # List of required Python libraries
├── .gitignore                    # Files and directories to be ignored by Git
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
1. Run the main script to execute the data pipeline:
   ```bash
   python src/main.py
   ```
2. The generated visualizations will be saved in the `plots/` folder.

## Contributing
We welcome contributions! Please review our [Code of Conduct](docs/code_of_conduct.md) and follow the [Contributing Guidelines](docs/contributing.md).

### Git Workflow
- **`main`**: Contains the stable version of the project.
- **`develop`**: Main development branch.
- **`feature/<feature-name>`**: Branch for new features.

### Commit Message Conventions
Follow the [Conventional Commits](https://www.conventionalcommits.org/) standard:
- `feat`: Introduces a new feature.
- `fix`: Fixes a bug.
- `chore`: Updates to configuration files, documentation, or other non-code elements.

## Visual Aids
![Data Flowchart](docs/images/data_pipeline_flowchart.png)

## Resources
### Data Visualization in Python
- [GeeksforGeeks Tutorial](https://www.geeksforgeeks.org/python-data-visualization-tutorial/?utm_source=chatgpt.com) - Comprehensive guide on Python data visualization libraries.
- [Simplilearn Gids](https://www.simplilearn.com/tutorials/python-tutorial/data-visualization-in-python?utm_source=chatgpt.com) - Overview of different visualization techniques.
- [MIT Tutorial](https://www.mit.edu/~amidi/teaching/data-science-tools/tutorial/data-visualization-with-python/?utm_source=chatgpt.com) - Advanced plotting and customization.
- [DataCamp Track](https://www.datacamp.com/tracks/data-visualization-with-python?utm_source=chatgpt.com) - Practical learning path for visualization.

### Python Project Structure
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/?utm_source=chatgpt.com) - Best practices for organizing Python projects.
- [Medium Artikel over Best Practices](https://medium.com/%40kuldeepkumawat195/best-practices-in-structuring-python-projects-c7232c9304b0?utm_source=chatgpt.com) - Improving readability and maintainability.
- [ArjanCodes Blog](https://arjancodes.com/blog/organizing-python-code-with-packages-and-modules/?utm_source=chatgpt.com) - Organizing Python code effectively.

### Version Control Best Practices
- [HopHR Tutorial](https://www.hophr.com/tutorial-page/best-practices-version-control-python-projects-step-by-step-guide?utm_source=chatgpt.com) - Guidelines for Git workflows.

### Video Tutorial
- [Python Data Visualization Full Course](https://www.youtube.com/watch?v=q68Qundmans&utm_source=chatgpt.com) - Comprehensive course for data visualization.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
- Rowan Biets
---

