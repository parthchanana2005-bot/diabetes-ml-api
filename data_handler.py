import pandas as pd
import os

def save_data(new_data):

    file_path = "data_store.csv"

    # Convert incoming data to DataFrame
    new_df = pd.DataFrame([new_data])

    # If file exists → append
    if os.path.exists(file_path):
        existing_df = pd.read_csv(file_path)
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    else:
        updated_df = new_df

    # Save back
    updated_df.to_csv(file_path, index=False)