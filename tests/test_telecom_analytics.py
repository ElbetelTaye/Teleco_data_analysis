import unittest
from unittest.mock import patch
import pandas as pd

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.telecom_analytics import (fetch_data_from_db, clean_and_transform_data, 
                                       aggregate_user_engagement, perform_clustering, 
                                       summarize_clusters)


class TestTelecomAnalytics(unittest.TestCase):

    @patch('scripts.telecom_analytics.psycopg2.connect')
    def test_fetch_data_from_db(self, mock_connect):
        # Example mock test for fetch_data_from_db
        mock_connect.return_value.cursor.return_value.fetchall.return_value = [
            (1, 1000, 2000, 3000),
            (2, 2000, 3000, 4000)
        ]
        df = fetch_data_from_db('test_db', 'user', 'password', 'host', 'SELECT * FROM table')
        self.assertIsInstance(df, pd.DataFrame)

    def test_clean_and_transform_data(self):
        df = pd.DataFrame({
            'MSISDN/Number': [123, 456, 789],
            'Dur. (ms)': [1000, None, 500],
            'Total DL (Bytes)': [2000, None, 1000],
            'Total UL (Bytes)': [1000, 2000, None]
        })
        cleaned_df = clean_and_transform_data(df)
        self.assertIn('total_traffic', cleaned_df.columns)
        self.assertFalse(cleaned_df.isnull().values.any())

    def test_aggregate_user_engagement(self):
        df = pd.DataFrame({
            'MSISDN/Number': [123, 123, 456],
            'session_duration': [1000, 500, 1500],
            'total_traffic': [2000, 1000, 2500]
        })
        aggregated_df = aggregate_user_engagement(df)
        self.assertEqual(len(aggregated_df), 2)

    @patch('scripts.telecom_analytics.KMeans')
    def test_perform_clustering(self, MockKMeans):
        df = pd.DataFrame({
            'MSISDN/Number': [123, 456],
            'session_duration': [1000, 2000],
            'total_traffic': [3000, 4000]
        })
        mock_kmeans = MockKMeans.return_value
        mock_kmeans.fit_predict.return_value = [0, 1]
        clustered_df = perform_clustering(df, 2)
        self.assertIn('cluster', clustered_df.columns)

  


if __name__ == '__main__':
    unittest.main()
