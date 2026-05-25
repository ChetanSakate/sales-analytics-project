import pandas as pd

def load_dataset(file_path):

    df = pd.read_csv(file_path)

    print(f"Dataset loaded successfully.")
    print(f"Rows Loaded: {len(df)}")

    return df