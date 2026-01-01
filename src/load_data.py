import pandas as pd

def load_covid_data(csv_path: str) -> pd.DataFrame:
    """
    Load US COVID-19 confirmed cases time series data.
    """
    df = pd.read_csv(csv_path)
    return df
