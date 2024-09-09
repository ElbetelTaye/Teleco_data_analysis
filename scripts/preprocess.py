import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd

#Prepare the data for clustering by selecting the specified columns.
def prepare_clustering_data(df, columns):

    return df[columns]

#Normalize the data using StandardScaler.
def normalize_data(data):
    scaler = StandardScaler()
    
    return scaler.fit_transform(data)

#Apply K-means clustering to the data and return the cluster labels.
def apply_kmeans_clustering(data, n_clusters=3, random_state=0):
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    return kmeans.fit_predict(data)

#Analyze the clusters by calculating the mean of numeric columns grouped by clusters.
def analyze_clusters(df, numeric_columns):
    
    return df.groupby('Cluster')[numeric_columns].mean()

#Aggregate average throughput by handset type.
def aggregate_throughput_by_handset_type(df):
    
    return df.groupby('Handset Type').agg({
        'Avg Throughput DL (kbps)': 'mean',
        'Avg Throughput UL (kbps)': 'mean'
    }).reset_index()

#Fill missing values in the specified column with the mean of that column.
def fill_missing_values(df, column_name):
    
    df[column_name].fillna(df[column_name].mean(), inplace=True)

#Aggregate the data per customer by taking the mean of specified columns.
def aggregate_data(df, group_by_column, agg_columns):
    
    return df.groupby(group_by_column).agg(agg_columns).reset_index()

#Get the top N largest values in the specified column.
def get_top_n_values(df, column_name, n=10):
    
    return df.nlargest(n, column_name)

#Get the bottom N smallest values in the specified column.
def get_bottom_n_values(df, column_name, n=10):
    
    return df.nsmallest(n, column_name)

#Get the most frequent value in the specified column.
def get_most_frequent_value(df, column_name):
    
    return df[column_name].mode()

#Rename columns of the DataFrame.
def rename_columns(df, new_column_names):
    
    df.columns = new_column_names