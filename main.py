import mylib.data_utils as data_utils
import mylib.stats_utils as stats_utils
import mylib.visualization as visualization
import logging


def main():
    # Setup logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Load the dataset
    logger.info("Loading dataset...")
    data = data_utils.load_data("US_birth.csv")

    # Display basic information
    logger.info(f"Dataset Shape: {data.shape}")
    logger.info(f"Columns: {data.columns}")

    # Calculate and display statistics
    mean_births = stats_utils.calculate_mean(data, "births")
    median_births = stats_utils.calculate_median(data, "births")
    logger.info(f"Mean Births: {mean_births}")
    logger.info(f"Median Births: {median_births}")

    # Filter data for a specific year
    logger.info("Filtering data for the year 2005...")
    data_2005 = data_utils.filter_data(data, year=2005)
    logger.info("Filtered Data (Year 2005):")
    logger.info(data_2005.head())

    # Plot the birth trends over time
    logger.info("Plotting birth trends over time...")
    visualization.plot_birth_trends(data)


if __name__ == "__main__":
    main()
