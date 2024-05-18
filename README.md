# Environmental Data Analysis Tool

This repository contains a Python application that utilizes the Google Earth Engine API, Streamlit, and various datasets to analyze environmental metrics across different regions of Africa. The tool allows users to select a region (West Africa, East Africa, Southern Africa) and visualize key environmental indicators such as land area, greenhouse gas emissions, precipitation, air pollution, and surface temperature over time. Additionally, it calculates and displays correlations between these metrics.

## Features

- **Environmental Metric Visualization**: Users can view trends in land area, greenhouse gas emissions, precipitation, air pollution, and surface temperature over time for each selected region.
- **Correlation Analysis**: The tool computes and visualizes correlations between different environmental metrics to identify potential relationships and patterns.
- **Interactive Selection**: A sidebar allows users to easily switch between West Africa, East Africa, and Southern Africa to compare regional differences.

## Requirements

- Python 3.x
- Streamlit
- Google Earth Engine (GEE) Python API (`ee` package)
- Pandas
- Numpy
- Plotly

## Installation

To run this application locally, you need to have Python installed on your machine. Then, install the required packages using pip:

````bash ````
pip install streamlit earthengine-api pandas numpy plotly


Before running the application, ensure you have authenticated with Google Earth Engine by visiting `https://code.earthengine.google.com/` and following the authentication steps.

## Usage

1. Clone this repository to your local machine.
2. Open a terminal or command prompt in the project directory.
3. Run the application using Streamlit:

````bash ````
streamlit run main.py


4. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`) to interact with the application.

## Contributing

Contributions to improve the functionality, add new features, or enhance the analysis capabilities are welcome. Please submit a pull request detailing the proposed changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
