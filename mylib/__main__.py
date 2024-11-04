from mylib.data_utils import load_data
from mylib.stats_utils import calculate_mean, calculate_median
from mylib.visualization import plot_birth_trends


def main():
    # Example usage of the functions in mylib
    data = load_data("US_birth.csv")
    mean_births = calculate_mean(data, "births")
    median_births = calculate_median(data, "births")
    print(f"Mean Births: {mean_births}")
    print(f"Median Births: {median_births}")
    plot_birth_trends(data)


if __name__ == "__main__":
    main()
