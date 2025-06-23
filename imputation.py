import pandas as pd

class DataImputation:
    def __init__(self, data):
        self.data = data

    def show_null_counts(self):
        try:
            print("\nNumber of NULL values in each column:")
            print(self.data.isnull().sum())
        except Exception as e:
            print(f"Error showing null counts: {e}")

    def remove_column(self, col):
        try:
            if col not in self.data.columns:
                print(f"Column '{col}' not found.")
                return
            self.data = self.data.drop(columns=[col])
            print(f"Column '{col}' removed.")
        except Exception as e:
            print(f"Error removing column '{col}': {e}")

    def fill_null_mean(self, col):
        try:
            if col not in self.data.columns:
                print(f"Column '{col}' not found.")
                return
            if not pd.api.types.is_numeric_dtype(self.data[col]):
                print(f"Column '{col}' is not numeric.")
                return
            mean_val = self.data[col].mean()
            self.data[col] = self.data[col].fillna(mean_val)
            print(f"Filled NULLs in '{col}' with mean: {mean_val}")
        except Exception as e:
            print(f"Error filling nulls with mean in '{col}': {e}")

    def fill_null_median(self, col):
        try:
            if col not in self.data.columns:
                print(f"Column '{col}' not found.")
                return
            if not pd.api.types.is_numeric_dtype(self.data[col]):
                print(f"Column '{col}' is not numeric.")
                return
            median_val = self.data[col].median()
            self.data[col] = self.data[col].fillna(median_val)
            print(f"Filled NULLs in '{col}' with median: {median_val}")
        except Exception as e:
            print(f"Error filling nulls with median in '{col}': {e}")

    def fill_null_mode(self, col):
        try:
            if col not in self.data.columns:
                print(f"Column '{col}' not found.")
                return
            mode_val = self.data[col].mode()
            if mode_val.empty:
                print(f"No mode found for column '{col}'.")
                return
            mode_val = mode_val[0]
            self.data[col] = self.data[col].fillna(mode_val)
            print(f"Filled NULLs in '{col}' with mode: {mode_val}")
        except Exception as e:
            print(f"Error filling nulls with mode in '{col}': {e}")

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