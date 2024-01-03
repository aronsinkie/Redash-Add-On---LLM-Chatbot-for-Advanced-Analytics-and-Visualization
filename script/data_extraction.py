import pandas as pd

class DataFrameManipulator:
    def __init__(self, df):
        self.df = df

    def rename_columns(self, new_column_names):
        """
        Rename columns in the Pandas DataFrame.

        Parameters:
        - new_column_names: Dictionary of old-to-new column names
        """
        self.df.rename(columns=new_column_names, inplace=True)

    def drop_rows(self, rows_to_drop, by_index=True):
        """
        Drop rows from the Pandas DataFrame.

        Parameters:
        - rows_to_drop: List of index labels or row numbers to drop
        - by_index: If True, drop rows by index labels; if False, drop rows by row numbers
        """
        if by_index:
            self.df = self.df.drop(rows_to_drop)
        else:
            self.df = self.df.drop(self.df.index[rows_to_drop])



