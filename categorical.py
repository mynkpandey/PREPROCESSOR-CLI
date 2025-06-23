import pandas as pd

class CategoricalEncoder:
    def __init__(self, data):
        self.data = data

    def show_categorical_columns(self):
        try:
            cat_cols = self.data.select_dtypes(include=['object', 'category']).columns.tolist()
            if not cat_cols:
                print("No categorical columns found.")
            else:
                print("\nCategorical columns:")
                print(' '.join(cat_cols))
        except Exception as e:
            print(f"Error showing categorical columns: {e}")

    def one_hot_encode(self, col):
        try:
            if col not in self.data.columns:
                print(f"Column '{col}' not found.")
                return
            if not pd.api.types.is_object_dtype(self.data[col]) and not pd.api.types.is_categorical_dtype(self.data[col]):
                print(f"Column '{col}' is not categorical.")
                return
            self.data = pd.get_dummies(self.data, columns=[col], drop_first=False)
            print(f"One hot encoding performed on column '{col}'.")
        except Exception as e:
            print(f"Error in one hot encoding for column '{col}': {e}")

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