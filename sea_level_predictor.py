import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    x, y = df["Year"], df["CSIRO Adjusted Sea Level"]
    plt.scatter(x=x, y=y)
    # Create first line of best fit
    res = linregress(x, y)
    x = pd.Series(range(x[0], 2051))
    plt.plot(x, res.intercept + res.slope * x)
    # Create second line of best fit
    start_year = 2000
    x, y = df[df["Year"] >= start_year]["Year"], df[df["Year"] >= start_year]["CSIRO Adjusted Sea Level"]
    res = linregress(x, y)
    x = pd.Series(range(start_year, 2051))
    plt.plot(x, res.intercept + res.slope * x)
    # Add labels and title

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()