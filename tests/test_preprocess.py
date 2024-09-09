import unittest
import pandas as pd
from scripts.preprocess import (
    prepare_clustering_data, normalize_data, apply_kmeans_clustering,
    analyze_clusters, aggregate_throughput_by_handset_type, fill_missing_values,
    aggregate_data, get_top_n_values, get_bottom_n_values, get_most_frequent_value,
    rename_columns
)
from sklearn.preprocessing import StandardScaler
import numpy as np


class TestPreprocessFunctions(unittest.TestCase):

    def setUp(self):
        # Sample data to be used across multiple test cases
        self.df = pd.DataFrame({
            'MSISDN/Number': [1, 2, 3, 4],
            'Avg TCP DL Retransmission': [10, 20, np.nan, 40],
            'Avg TCP UL Retransmission': [5, np.nan, 25, 35],
            'Avg RTT DL (ms)': [100, 150, 200, np.nan],
            'Avg RTT UL (ms)': [50, np.nan, 150, 200],
            'Avg Throughput DL (kbps)': [500, 600, np.nan, 800],
            'Avg Throughput UL (kbps)': [250, np.nan, 350, 400],
            'Handset Type': ['TypeA', 'TypeB', 'TypeA', 'TypeC']
        })

    def test_prepare_clustering_data(self):
        columns = ['Avg TCP DL Retransmission', 'Avg TCP UL Retransmission']
        clustering_data = prepare_clustering_data(self.df, columns)
        self.assertTrue(all(clustering_data.columns == columns))

    def test_normalize_data(self):
        data = self.df[['Avg TCP DL Retransmission', 'Avg TCP UL Retransmission']].fillna(0)
        normalized_data = normalize_data(data)
        scaler = StandardScaler().fit(data)
        expected_normalized_data = scaler.transform(data)
        np.testing.assert_almost_equal(normalized_data, expected_normalized_data)

    def test_apply_kmeans_clustering(self):
        data = self.df[['Avg TCP DL Retransmission', 'Avg TCP UL Retransmission']].fillna(0)
        normalized_data = normalize_data(data)
        cluster_labels = apply_kmeans_clustering(normalized_data, n_clusters=2, random_state=0)
        self.assertEqual(len(cluster_labels), len(self.df))

    def test_analyze_clusters(self):
        self.df['Cluster'] = [0, 0, 1, 1]
        numeric_columns = ['Avg TCP DL Retransmission', 'Avg TCP UL Retransmission']
        cluster_analysis = analyze_clusters(self.df, numeric_columns)
        self.assertTrue('Avg TCP DL Retransmission' in cluster_analysis.columns)

    def test_aggregate_throughput_by_handset_type(self):
        throughput_data = aggregate_throughput_by_handset_type(self.df)
        self.assertEqual(len(throughput_data), 3)

    def test_fill_missing_values(self):
        fill_missing_values(self.df, 'Avg TCP DL Retransmission')
        self.assertFalse(self.df['Avg TCP DL Retransmission'].isnull().any())

    def test_aggregate_data(self):
        agg_columns = {'Avg TCP DL Retransmission': 'mean', 'Avg TCP UL Retransmission': 'mean'}
        aggregated_data = aggregate_data(self.df, 'Handset Type', agg_columns)
        self.assertTrue('Avg TCP DL Retransmission' in aggregated_data.columns)

    def test_get_top_n_values(self):
        top_values = get_top_n_values(self.df, 'Avg TCP DL Retransmission', n=2)
        self.assertEqual(len(top_values), 2)

    def test_get_bottom_n_values(self):
        bottom_values = get_bottom_n_values(self.df, 'Avg TCP DL Retransmission', n=2)
        self.assertEqual(len(bottom_values), 2)

    def test_get_most_frequent_value(self):
        most_frequent = get_most_frequent_value(self.df, 'Handset Type')
        self.assertEqual(most_frequent.values[0], 'TypeA')

    def test_rename_columns(self):
        new_column_names = ['Number', 'DL Retrans', 'UL Retrans', 'RTT DL', 'RTT UL', 'Throughput DL', 'Throughput UL', 'Handset']
        rename_columns(self.df, new_column_names)
        self.assertTrue(all(self.df.columns == new_column_names))


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
