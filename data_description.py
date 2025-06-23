import pandas as pd

class DataDescription:
    def __init__(self, data):
        self.data = data

    def describe_all_columns(self):
        try:
            print("\nColumn Properties:")
            desc = self.data.describe(include='all').T
            nulls = self.data.isnull().sum()
            dtypes = self.data.dtypes
            desc['null_count'] = nulls
            desc['dtype'] = dtypes
            print(desc[['dtype', 'null_count', 'count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']].fillna('-'))
        except Exception as e:
            print(f"Error describing all columns: {e}")

    def describe_column(self, col):
        try:
            if col not in self.data.columns:
                print(f"Column '{col}' not found.")
                return
            dtype = self.data[col].dtype
            print(f"\nProperties for column '{col}':")
            if pd.api.types.is_numeric_dtype(self.data[col]):
                print(f"  Mean: {self.data[col].mean()}")
                print(f"  Std: {self.data[col].std()}")
                print(f"  Min: {self.data[col].min()}")
                print(f"  25%: {self.data[col].quantile(0.25)}")
                print(f"  50%: {self.data[col].median()}")
                print(f"  75%: {self.data[col].quantile(0.75)}")
                print(f"  Max: {self.data[col].max()}")
                print(f"  Count: {self.data[col].count()}")
                print(f"  Nulls: {self.data[col].isnull().sum()}")
                print(f"  Dtype: {dtype}")
            else:
                print(f"  Count: {self.data[col].count()}")
                print(f"  Unique: {self.data[col].nunique()}")
                print(f"  Nulls: {self.data[col].isnull().sum()}")
                print(f"  Dtype: {dtype}")
        except Exception as e:
            print(f"Error describing column '{col}': {e}")

    def show_n_rows(self, n):
        try:
            n = int(n)
            if n < 1:
                print("Number of rows must be positive.")
                return
            print(f"\nFirst {n} rows of the dataset:")
            print(self.data.head(n))
        except Exception as e:
            print(f"Error showing rows: {e}") 