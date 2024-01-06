import unittest
import pandas as pd

class TestDataFrameManipulator(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
        self.df = pd.DataFrame(data)
        self.df_manipulator = DataFrameManipulator(self.df.copy())

    def test_rename_columns(self):
        # Test renaming columns
        new_column_names = {'A': 'X', 'B': 'Y', 'C': 'Z'}
        modified_df = self.df_manipulator.rename_columns(new_column_names)
        expected_columns = ['X', 'Y', 'Z']
        self.assertListEqual(list(modified_df.columns), expected_columns)

    def test_drop_rows_by_index(self):
        # Test dropping rows by index
        rows_to_drop = [0, 2]
        modified_df = self.df_manipulator.drop_rows(rows_to_drop)
        expected_df = pd.DataFrame({'A': [2], 'B': [5], 'C': [8]}, index=[1])
        pd.testing.assert_frame_equal(modified_df, expected_df)

    def test_drop_rows_by_row_numbers(self):
        # Test dropping rows by row numbers
        rows_to_drop = [0, 2]
        modified_df = self.df_manipulator.drop_rows(rows_to_drop, by_index=False)
        expected_df = pd.DataFrame({'A': [2], 'B': [5], 'C': [8]}, index=[1])
        pd.testing.assert_frame_equal(modified_df, expected_df)

    def test_drop_columns(self):
        # Test dropping columns
        columns_to_drop = ['A', 'C']
        modified_df = self.df_manipulator.drop_columns(columns_to_drop)
        expected_df = pd.DataFrame({'B': [4, 5, 6]})
        pd.testing.assert_frame_equal(modified_df, expected_df)

if __name__ == '__main__':
    unittest.main()