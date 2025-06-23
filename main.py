import os
import pandas as pd
from data_description import DataDescription
from imputation import DataImputation
from categorical import CategoricalEncoder
from feature_scaling import FeatureScaler
from download import DownloadDataset
import tkinter as tk
from tkinter import filedialog

class MainPreprocessor:
    def __init__(self):
        self.data = None
        self.target = None
        self.target_column = None

    def input_csv(self):
        while True:
            print("Please select your CSV file from the file explorer window.")
            root = tk.Tk()
            root.withdraw()  # Hide the main window
            file_path = filedialog.askopenfilename(
                title="Select CSV file",
                filetypes=[("CSV files", "*.csv")]
            )
            root.destroy()
            if not file_path:
                retry = input("No file selected. Try again? (y/n): ")
                if retry.lower() != 'y':
                    print("Exiting...")
                    exit(0)
                continue
            if not file_path.endswith('.csv'):
                print("Input file must be a .csv file.")
                continue
            if not os.path.exists(file_path):
                print(f"File '{file_path}' does not exist.")
                continue
            try:
                self.data = pd.read_csv(file_path)
                break
            except Exception as e:
                print(f"Error loading CSV: {e}")
                continue

    def choose_target_variable(self):
        try:
            if self.data is None:
                raise ValueError("Data not loaded. Please check the CSV loading step.")
            print("\nColumns \U0001F447")
            print(' '.join(self.data.columns))
            while True:
                target = input("Which is the target variable:(Press -1 to exit) ")
                if target == "-1":
                    print("Exiting...")
                    exit(0)
                if target not in self.data.columns:
                    print(f"Column '{target}' not found in dataset. Try again.")
                    continue
                confirm = input("Are you sure? (y/n) ")
                if confirm.lower() == 'y':
                    self.target = self.data[target]
                    self.data = self.data.drop(columns=[target])
                    self.target_column = target
                    print("Done.......\U0001F60A\n")
                    break
                else:
                    print("Cancelled. Please select again.")
        except Exception as e:
            print(f"Error choosing target variable: {e}")
            exit(1)

    def data_description_menu(self):
        dd = DataDescription(self.data)
        while True:
            print("\nTasks (Data Description)\U0001F447")
            print("1. Describe a specific Column")
            print("2. Show Properties of Each Column")
            print("3. Show the Dataset")
            choice = input("\nWhat you want to do? (Press -1 to go back) ")
            if choice == "-1":
                break
            elif choice == "1":
                col = input("Enter column name: ")
                dd.describe_column(col)
            elif choice == "2":
                dd.describe_all_columns()
            elif choice == "3":
                n = input("Enter number of rows to display: ")
                dd.show_n_rows(n)
            else:
                print("Invalid choice. Please select a valid option.")

    def imputation_menu(self):
        imputer = DataImputation(self.data)
        while True:
            print("\nImputation Tasks\U0001F447")
            print("1. Show number of Null Values")
            print("2. Remove Columns")
            print("3. Fill Null Values (with mean)")
            print("4. Fill Null Values (with median)")
            print("5. Fill Null Values (with mode)")
            print("6. Show the Dataset")
            choice = input("\nWhat you want to do? (Press -1 to go back) ")
            if choice == "-1":
                self.data = imputer.data
                break
            elif choice == "1":
                imputer.show_null_counts()
            elif choice == "2":
                col = input("Enter column name to remove: ")
                imputer.remove_column(col)
            elif choice == "3":
                col = input("Enter column name to fill nulls with mean: ")
                imputer.fill_null_mean(col)
            elif choice == "4":
                col = input("Enter column name to fill nulls with median: ")
                imputer.fill_null_median(col)
            elif choice == "5":
                col = input("Enter column name to fill nulls with mode: ")
                imputer.fill_null_mode(col)
            elif choice == "6":
                n = input("Enter number of rows to display: ")
                imputer.show_n_rows(n)
            else:
                print("Invalid choice. Please select a valid option.")
        self.data = imputer.data

    def categorical_menu(self):
        encoder = CategoricalEncoder(self.data)
        while True:
            print("\nTasks\U0001F447")
            print("1. Show Categorical Columns")
            print("2. Performing One Hot encoding")
            print("3. Show the Dataset")
            choice = input("\nWhat you want to do? (Press -1 to go back) ")
            if choice == "-1":
                self.data = encoder.data
                break
            elif choice == "1":
                encoder.show_categorical_columns()
            elif choice == "2":
                col = input("Enter column name to one hot encode: ")
                encoder.one_hot_encode(col)
            elif choice == "3":
                n = input("Enter number of rows to display: ")
                encoder.show_n_rows(n)
            else:
                print("Invalid choice. Please select a valid option.")
        self.data = encoder.data

    def scaling_menu(self):
        scaler = FeatureScaler(self.data)
        while True:
            print("\nTasks (Feature Scaling)\U0001F447")
            print("1. Perform Normalization(MinMax Scaler)")
            print("2. Perform Standardization(Standard Scaler)")
            print("3. Show the Dataset")
            choice = input("\nWhat you want to do? (Press -1 to go back) ")
            if choice == "-1":
                self.data = scaler.data
                break
            elif choice == "1":
                cols = input("Enter column name(s) to normalize (comma-separated for multiple): ")
                scaler.normalize_columns(cols)
            elif choice == "2":
                cols = input("Enter column name(s) to standardize (comma-separated for multiple): ")
                scaler.standardize_columns(cols)
            elif choice == "3":
                n = input("Enter number of rows to display: ")
                scaler.show_n_rows(n)
            else:
                print("Invalid choice. Please select a valid option.")
        self.data = scaler.data

    def download_menu(self):
        downloader = DownloadDataset(self.data)
        while True:
            filename = input("Enter the FILENAME you want? (Press -1 to go back): ")
            if filename == "-1":
                print("Going back...")
                break
            success = downloader.save_to_csv(filename)
            if success:
                break

    def show_menu(self):
        while True:
            print("Tasks (Preprocessing)\U0001F447")
            print("1. Data Description")
            print("2. Handling NULL Values")
            print("3. Encoding Categorical Data")
            print("4. Feature Scaling of the Dataset")
            print("5. Download the modified dataset\n")
            choice = input("What do you want to do? (Press -1 to exit): ")
            if choice == "-1":
                print("Exiting...")
                exit(0)
            elif choice == "1":
                self.data_description_menu()
            elif choice == "2":
                self.imputation_menu()
            elif choice == "3":
                self.categorical_menu()
            elif choice == "4":
                self.scaling_menu()
            elif choice == "5":
                self.download_menu()
            else:
                print("Invalid choice. Please select a valid option.")

    def run(self):
        print("WELCOME TO THE MACHINE LEARNING PREPROCESSOR CLI!!!\U0001F60A")
        self.input_csv()
        self.choose_target_variable()
        self.show_menu()

if __name__ == "__main__":
    main_proc = MainPreprocessor()
    main_proc.run()
