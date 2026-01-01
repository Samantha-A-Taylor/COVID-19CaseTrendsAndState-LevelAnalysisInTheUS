import pandas as pd

def aggregate_state_cases(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total cases by state."""
    return (
        df.groupby("Province_State")["cases"]
        .max()
        .reset_index()
        .sort_values(by="cases", ascending=False)
    )

def regional_proportions(df: pd.DataFrame, region_map: dict) -> pd.DataFrame:
    """Calculate proportion of cases by region."""
    df = df.copy()
    df["region"] = df["Province_State"].map(region_map)
    region_totals = df.groupby("region")["cases"].max()
    proportions = region_totals / region_totals.sum()
    return proportions.reset_index(name="proportion")
