# Machine Learning Preprocessor CLI

A command-line interface (CLI) tool built with Python for interactively preprocessing machine learning datasets. This tool guides the user through common preprocessing steps, allowing them to clean and prepare their data for model training.

## Features

- **Interactive File Selection:** Opens a file explorer to securely select a local CSV file.
- **Target Variable Separation:** Choose and separate the target (dependent) variable from the features.
- **Data Description:** Get a statistical overview of the dataset.
  - View properties of all columns (mean, std, percentiles, nulls, etc.).
  - View properties of a specific column.
  - Display the first 'n' rows of the dataset.
- **Handling Null Values (Imputation):**
  - View columns with null values and their counts.
  - Remove columns with too many missing values.
  - Fill nulls with mean, median, or mode.
- **Encoding Categorical Data:**
  - View all categorical columns.
  - Perform One-Hot Encoding on selected columns.
- **Feature Scaling:**
  - Normalize data using `MinMaxScaler`.
  - Standardize data using `StandardScaler`.
- **Download Preprocessed Data:** Save the modified dataset to a new CSV file.

## Requirements

The project requires Python 3 and the following libraries:

- `pandas`
- `numpy`
- `scikit-learn`

`Tkinter` is also used for the file dialog and is part of the standard Python library, so no separate installation is needed.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/PREPROCESSOR-CLI.git
    cd PREPROCESSOR-CLI
    ```

2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main script from the project's root directory:

```bash
python main.py
```

The application will launch, opening a file explorer to select your CSV file. Follow the on-screen prompts to preprocess your data.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details. 