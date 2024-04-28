from logging import exception

import pandas as pd
from zenml import step

@step(enable_cache=False)
def ingest_data(Data_path:str) -> pd.DataFrame:
    try:

        Data = pd.read_csv(Data_path)
        Data = pd.DataFrame(Data.loc[:10000, :])
        return Data
    except Exception as e:
        print(f"Error during ingestion: {e}")
