# Population Data Pipeline

## Description
This pipeline processes and analyzes population data from the 2020 Census. It includes functionality to clean, process, and summarize the data efficiently.

## Files
- `population_pipeline.py`: Main script for running the population data pipeline.
- `test.py`: Unit tests for validating the pipeline's functionality.
- `us_pop_by_state.csv`: Dataset used as input for the pipeline.
- `requirements.txt`: List of Python dependencies required to run the project.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Islam-Ali98/population-data-pipeline.git
   cd population-data-pipeline
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   source venv/bin/activate      # On MacOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the pipeline with the following command:
```bash
python population_pipeline.py --input_file us_pop_by_state.csv --output_file processed_data.csv
```

## Testing
Run the test suite to validate the pipeline:
```bash
pytest test.py
```

## Features
- Loads population data from a CSV file.
- Cleans the dataset by removing missing values and standardizing column names.
- Processes the data to calculate summary statistics, including total population.
- Saves the processed data to a new CSV file.
