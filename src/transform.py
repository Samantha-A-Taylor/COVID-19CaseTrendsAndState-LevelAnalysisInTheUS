import pandas as pd

def filter_states(df: pd.DataFrame) -> pd.DataFrame:
    """Remove non-state rows such as territories."""
    return df[df["Province_State"].notna()]

def melt_time_series(df: pd.DataFrame) -> pd.DataFrame:
    """Convert wide date columns into long format."""
    id_vars = [
        "Province_State", "Country_Region",
        "Lat", "Long_", "Combined_Key"
    ]
    value_vars = df.columns[df.columns.str.match(r"\d+/\d+/\d+")]
    melted = df.melt(
        id_vars=id_vars,
        value_vars=value_vars,
        var_name="date",
        value_name="cases"
    )
    melted["date"] = pd.to_datetime(melted["date"])
    return melted

def filter_summer_2020(df: pd.DataFrame) -> pd.DataFrame:
    """Filter data for Summer 2020 (June–August)."""
    return df[
        (df["date"] >= "2020-06-01") &
        (df["date"] <= "2020-08-31")
    ]

def compute_weekly_increase(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate weekly case increases per state."""
    df = df.sort_values(["Province_State", "date"])
    df["weekly_increase"] = (
        df.groupby("Province_State")["cases"].diff(7)
    )
    return df
