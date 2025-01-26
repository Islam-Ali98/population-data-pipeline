import pytest
import pandas as pd
import os
from unittest.mock import patch
from population_pipeline import load_data, clean_data, process_data, save_data

@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame({
        'rank': [1, 2, 3],
        'state': ['California', 'Texas', 'Florida'],
        'state_code': ['CA', 'TX', 'FL'],
        '2020_census': [39538223, 29145505, 21538187],
        'percent_of_total': [0.1191, 0.0874, 0.0647]
    })

def test_load_data(sample_data):
    """Test the load_data function."""
    test_file = "us_pop_by_state.csv"
    sample_data.to_csv(test_file, index=False)
    
    # Load the data
    result = load_data(test_file)
    
    # Check the data matches
    assert result.equals(sample_data)

    # Cleanup
    os.remove(test_file)

def test_clean_data(sample_data):
    """Test the clean_data function."""
    # Introduce some missing values and spaces in column names
    sample_data_with_issues = sample_data.copy()
    sample_data_with_issues['rank'] = [1, None, 3]
    sample_data_with_issues.columns = [col + ' ' for col in sample_data_with_issues.columns]
    
    # Clean the data
    cleaned_data = clean_data(sample_data_with_issues)
    
    # Check for missing values removal
    assert cleaned_data.shape[0] == 2  # One row should be removed due to NaN in 'rank'

    # Check column names are standardized
    assert 'rank' in cleaned_data.columns
    assert 'state' in cleaned_data.columns
    assert 'state_code' in cleaned_data.columns
    assert '2020_census' in cleaned_data.columns
    assert 'percent_of_total' in cleaned_data.columns

def test_process_data(sample_data):
    """Test the process_data function."""
    # Process the data (sum the '2020_census' column)
    processed_data = process_data(sample_data)
    
    # Check that the total population is correctly calculated
    expected_total_population = 39538223 + 29145505 + 21538187
    assert processed_data['total_population'][0] == expected_total_population

@patch("population_pipeline.os.makedirs")  # Mocking os.makedirs to avoid actual file creation
@patch("population_pipeline.pd.DataFrame.to_csv")  # Mocking to_csv to avoid file writing
def test_save_data(mock_to_csv, mock_makedirs, sample_data):
    """Test the save_data function."""
    output_path = "output_dir/processed_data.csv"  # Include a directory in the path

    # Call save_data function
    save_data(sample_data, output_path)

    # Ensure os.makedirs was called to create the directory
    mock_makedirs.assert_called_once_with(os.path.dirname(output_path), exist_ok=True)

    # Ensure to_csv was called to save the data
    mock_to_csv.assert_called_once_with(output_path, index=False)


