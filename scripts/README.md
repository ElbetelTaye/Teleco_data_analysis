# Project Overview

This project is a Python-based data analysis and clustering pipeline that leverages the pandas library for data manipulation and the scikit-learn library for data preprocessing and clustering. The code provides various modular functions for tasks such as data aggregation, normalization, filling missing values, applying K-means clustering, and analyzing cluster characteristics.

## Requirements
To run the project, you need the following Python libraries:

- pandas
- scikit-learn
You can install them using pip:

    pip install pandas scikit-learn

### Functions

1. prepare_clustering_data(df, columns)
This function prepares the data for clustering by selecting the specified columns.

- Input:
    df: DataFrame containing the data.
    columns: List of columns to select.
    Output: DataFrame with selected columns.

2. normalize_data(data)
This function normalizes the data using StandardScaler from the scikit-learn library.

- Input:
    data: DataFrame or array-like object containing the data.
    Output: Normalized data as a NumPy array.

3. apply_kmeans_clustering(data, n_clusters=3, random_state=0)
This function applies K-means clustering to the data and returns the cluster labels.

- Input:
    data: Normalized data for clustering.
    n_clusters: Number of clusters (default is 3).
    random_state: Seed for random number generation (default is 0).
    Output: Array of cluster labels.

4. analyze_clusters(df, numeric_columns)
This function analyzes the clusters by calculating the mean of numeric columns grouped by cluster labels.

- Input:
    df: DataFrame containing the clustered data.
    numeric_columns: List of numeric columns to include in the analysis.
    Output: DataFrame with cluster-wise mean values for numeric columns.

5. aggregate_throughput_by_handset_type(df)
This function aggregates average throughput (both DL and UL) by handset type.

- Input:
    df: DataFrame containing the data.
    Output: DataFrame with aggregated throughput by handset type.

6. fill_missing_values(df, column_name)
This function fills missing values in the specified column with the mean of that column.

- Input:
    df: DataFrame containing the data.
    column_name: Name of the column with missing values.
    Output: None (modifies the DataFrame in place).

7. aggregate_data(df, group_by_column, agg_columns)
This function aggregates the data per customer by taking the mean of specified columns.

- Input:
    df: DataFrame containing the data.
    group_by_column: Column name to group by (e.g., customer ID).
    agg_columns: Dictionary specifying which columns to aggregate and how.
    Output: DataFrame with aggregated data per customer.

8. get_top_n_values(df, column_name, n=10)
This function returns the top N largest values in the specified column.

- Input:
    df: DataFrame containing the data.
    column_name: Column name for finding the top N values.
    n: Number of top values to retrieve (default is 10).
    Output: DataFrame with the top N values.

9. get_bottom_n_values(df, column_name, n=10)
This function returns the bottom N smallest values in the specified column.

- Input:
    df: DataFrame containing the data.
    column_name: Column name for finding the bottom N values.
    n: Number of bottom values to retrieve (default is 10).
    Output: DataFrame with the bottom N values.

10. get_most_frequent_value(df, column_name)
This function returns the most frequent value in the specified column.

- Input:
    df: DataFrame containing the data.
    column_name: Column name for finding the most frequent value.
    Output: The most frequent value in the column.

11. rename_columns(df, new_column_names)
This function renames the columns of the DataFrame.

- Input:
    df: DataFrame whose columns need to be renamed.
    new_column_names: List of new column names.
    Output: None (modifies the DataFrame in place).
