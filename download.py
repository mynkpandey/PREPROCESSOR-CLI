import pandas as pd

class DownloadDataset:
    def __init__(self, data):
        self.data = data

    def save_to_csv(self, filename):
        try:
            if filename == "-1":
                print("Going back...")
                return False
            if not filename.endswith('.csv'):
                print("Filename must end with .csv")
                return False
            self.data.to_csv(filename, index=False)
            print(f"Dataset saved as '{filename}'")
            return True
        except Exception as e:
            print(f"Error saving dataset: {e}")
            return False 