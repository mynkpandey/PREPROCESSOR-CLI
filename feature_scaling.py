import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class FeatureScaler:
    def __init__(self, data):
        self.data = data

    def normalize_columns(self, columns):
        try:
            cols = [col.strip() for col in columns.split(',')]
            for col in cols:
                if col not in self.data.columns:
                    print(f"Column '{col}' not found.")
                    return
                if not pd.api.types.is_numeric_dtype(self.data[col]):
                    print(f"Column '{col}' is not numeric.")
                    return
            scaler = MinMaxScaler()
            self.data[cols] = scaler.fit_transform(self.data[cols])
            print(f"Normalization (MinMaxScaler) performed on columns: {', '.join(cols)}")
        except Exception as e:
            print(f"Error normalizing columns: {e}")

    def standardize_columns(self, columns):
        try:
            cols = [col.strip() for col in columns.split(',')]
            for col in cols:
                if col not in self.data.columns:
                    print(f"Column '{col}' not found.")
                    return
                if not pd.api.types.is_numeric_dtype(self.data[col]):
                    print(f"Column '{col}' is not numeric.")
                    return
            scaler = StandardScaler()
            self.data[cols] = scaler.fit_transform(self.data[cols])
            print(f"Standardization (StandardScaler) performed on columns: {', '.join(cols)}")
        except Exception as e:
            print(f"Error standardizing columns: {e}")

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