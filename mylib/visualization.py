import matplotlib.pyplot as plt


def plot_birth_trends(data):
    """Plot the number of births over time."""
    plt.figure(figsize=(10, 6))
    data.groupby("year")["births"].sum().plot()
    plt.xlabel("Year")
    plt.ylabel("Total Births")
    plt.title("Birth Trends Over Time")
    plt.show()
