import matplotlib.pyplot as plt

def plot_weekly_trends(df):
    plt.figure(figsize=(10, 6))
    for state in df["Province_State"].unique():
        subset = df[df["Province_State"] == state]
        plt.plot(subset["date"], subset["weekly_increase"], alpha=0.3)

    plt.title("Weekly COVID-19 Case Increases by State (Summer 2020)")
    plt.xlabel("Date")
    plt.ylabel("Weekly Increase")
    plt.tight_layout()
    plt.show()
