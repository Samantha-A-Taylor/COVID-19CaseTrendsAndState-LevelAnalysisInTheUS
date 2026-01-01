from load_data import load_covid_data
from transform import (
    filter_states,
    melt_time_series,
    filter_summer_2020,
    compute_weekly_increase
)
from analysis import aggregate_state_cases
from visualization import plot_weekly_trends

DATA_PATH = "data/time_series_covid19_confirmed_US.csv"

def main():
    df = load_covid_data(DATA_PATH)
    df = filter_states(df)
    df = melt_time_series(df)
    df = filter_summer_2020(df)
    df = compute_weekly_increase(df)

    state_totals = aggregate_state_cases(df)
    print(state_totals.head(10))

    plot_weekly_trends(df)

if __name__ == "__main__":
    main()
