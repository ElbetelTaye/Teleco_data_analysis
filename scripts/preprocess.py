import pandas as pd

def fill_missing_values(df, column_name):
    """
    Fill missing values in the specified column with the mean of that column.
    """
    df[column_name].fillna(df[column_name].mean(), inplace=True)

def aggregate_data(df, group_by_column, agg_columns):
    """
    Aggregate the data per customer by taking the mean of specified columns.
    """
    return df.groupby(group_by_column).agg(agg_columns).reset_index()

def rename_columns(df, new_column_names):
    """
    Rename columns of the DataFrame.
    """
    df.columns = new_column_names