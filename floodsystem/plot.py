
"""Submodule used for creating plots of monitoring station data:"""

from floodsystem.station import  MonitoringStation
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit

def lables_and_title(title):
    """Adds date to x axis, Water level to the yaxis, rotates x tages 45 degrees and addes a title"""
    plt.xlabel("Date (YYYY-MM-DD)")
    plt.ylabel("Water Level (m)")
    plt.xticks(rotation=45)
    plt.title(title)
    return

def plot_high_low(dates, low, high):
    """For a x axis of dates, adds high and low marks"""
    list = []
    for i in range (0, len(dates)):
        list.append(low)
    plt.plot(dates, list)
    list = []
    for i in range (0, len(dates)):
        list.append(high)
    plt.plot(dates, list)


def plot_water_levels(station, dates, levels):
    """Plots water levlels at a Station, where station is a monitoring station object;
    dates are a list of dates
    levels are a corresponding list of levels"""

    plt.plot(dates, levels)
    #Plot low and high
    if station.typical_range_consistent:
        plot_high_low(dates, station.typical_range[0], station.typical_range[1])
    lables_and_title(station.name)
    plt.tight_layout()
    plt.show()

    

def plot_water_level_with_fit(station, dates, levels, p, high_low =False):
    """Plots water levlels at a Station, where station is a monitoring station object;
    dates are a list of dates
    levels are a corresponding list of levels
    Also ploys the polynomial line of best fit to degree p"""

    plt.plot(dates, levels)

    polyline = polyfit(dates, levels, p)

    if station.typical_range_consistent and high_low:
        plot_high_low(dates, station.typical_range[0], station.typical_range[1])

    # Lables
    lables_and_title(station.name)
    plt.tight_layout()
    plt.show()

