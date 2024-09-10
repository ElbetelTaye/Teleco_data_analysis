import pytest
import pandas as pd
import numpy as np
from unittest.mock import patch, MagicMock

from process import (
    top_5_handsets_per_manufacturer,
    fetch_data_from_db,
    remove_duplicates_and_undefined,
    handle_missing_values,
    handle_outliers,
    check_invalid_data,
    clean_data,
    top_handsets_used,
    top_handset_manufacturers,
    user_behavior_on_applications
)

# Sample data for testing
@pytest.fixture
def sample_df():
    data = {
        'Handset Manufacturer': ['Apple', 'Samsung', 'Huawei', 'Apple', 'Samsung'],
        'Handset Type': ['iPhone X', 'Galaxy S9', 'P30', 'iPhone 11', 'Galaxy S10'],
        'IMEI': [1, 2, 3, 4, 5],
        'Total DL (Bytes)': [500, 1000, 1500, 2000, 2500],
        'Total UL (Bytes)': [100, 200, 300, 400, 500],
        'Dur. (ms)': [1000, 2000, 3000, 4000, 5000]
    }
    return pd.DataFrame(data)

# Test top_5_handsets_per_manufacturer
def test_top_5_handsets_per_manufacturer(sample_df):
    top_manufacturers = ['Apple', 'Samsung']
    result = top_5_handsets_per_manufacturer(sample_df, top_manufacturers)
    assert len(result) == 4  # There should be 4 handsets in total (2 for Apple, 2 for Samsung)

# Test fetch_data_from_db
@patch('process.psycopg2.connect')
def test_fetch_data_from_db(mock_connect):
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn
    query = "SELECT * FROM handset_data"
    mock_df = pd.DataFrame({'Handset Manufacturer': ['Apple'], 'IMEI': [123]})
    mock_conn.cursor().fetchall.return_value = mock_df
    result = fetch_data_from_db('dbname', 'user', 'password', 'host', query)
    assert not result.empty
    mock_conn.close.assert_called_once()

# Test remove_duplicates_and_undefined
def test_remove_duplicates_and_undefined(sample_df):
    sample_df.loc[5] = ['undefined', 'undefined', 6, 3000, 600, 6000]  # Add a row with 'undefined'
    result = remove_duplicates_and_undefined(sample_df)
    assert 'undefined' not in result['Handset Manufacturer'].values
    assert result.shape[0] == 5  # Duplicates should be removed

# Test handle_missing_values
def test_handle_missing_values(sample_df):
    sample_df.loc[0, 'Total DL (Bytes)'] = np.nan  # Introduce a missing value
    result = handle_missing_values(sample_df)
    assert not result.isnull().values.any()  # Ensure no missing values remain

# Test handle_outliers
def test_handle_outliers(sample_df):
    sample_df.loc[0, 'Total DL (Bytes)'] = 1000000  # Introduce an outlier
    result = handle_outliers(sample_df)
    assert 1000000 not in result['Total DL (Bytes)'].values  # Outlier should be removed

# Test check_invalid_data
def test_check_invalid_data(sample_df):
    sample_df.loc[0, 'Total DL (Bytes)'] = -500  # Introduce invalid data
    result = check_invalid_data(sample_df)
    assert len(result) == 4  # Invalid row should be removed

# Test clean_data
def test_clean_data(sample_df):
    result = clean_data(sample_df)
    assert result.shape[0] <= sample_df.shape[0]  # Ensure data is cleaned

# Test top_handsets_used
def test_top_handsets_used(sample_df):
    result = top_handsets_used(sample_df)
    assert result.shape[0] == 5  # Ensure it returns the top handsets used

# Test top_handset_manufacturers
def test_top_handset_manufacturers(sample_df):
    result = top_handset_manufacturers(sample_df)
    assert result.shape[0] == 2  # Ensure it returns the top 3 manufacturers

# Test user_behavior_on_applications
def test_user_behavior_on_applications(sample_df):
    result = user_behavior_on_applications(sample_df)
    assert 'total_sessions' in result.columns
    assert 'total_download' in result.columns
