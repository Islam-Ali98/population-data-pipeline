import os
import pandas as pd
import argparse

def load_data(file_path):
    """Load the dataset from a CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean the dataset by handling missing values and standardizing column names."""
    # Drop rows with missing values
    df = df.dropna()

    # Standardize column names
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

    return df

def process_data(df):
    """Process the dataset, e.g., summarize total population."""
    # Summarize data: total population (2020_census)
    total_population = df['2020_census'].sum()

    # Optionally, you can add other summary statistics here
    summary = pd.DataFrame({'total_population': [total_population]})

    return summary

def save_data(df, output_path):
    """Save the processed data to a CSV file."""
    output_dir = os.path.dirname(output_path)
    if output_dir:  # Ensure the directory path exists
        os.makedirs(output_dir, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

def main(input_file, output_file):
    try:
        # Load the data
        print("Loading data...")
        raw_data = load_data(input_file)

        # Clean the data
        print("Cleaning data...")
        cleaned_data = clean_data(raw_data)

        # Process the data
        print("Processing data...")
        processed_data = process_data(cleaned_data)

        # Save the processed data
        print("Saving data...")
        save_data(processed_data, output_file)

        print("Pipeline executed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the population data pipeline.")
    parser.add_argument('--input_file', type=str, required=True, help="Path to the input CSV file.")
    parser.add_argument('--output_file', type=str, required=True, help="Path to save the processed CSV file.")
    
    args = parser.parse_args()

    main(args.input_file, args.output_file)
