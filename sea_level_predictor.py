import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    x_axis, y_axis = "Year", "CSIRO Adjusted Sea Level"
    plt.scatter(x=df[x_axis], y=df[y_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    # Create first line of best fit

    # Create second line of best fit

    # Add labels and title

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()