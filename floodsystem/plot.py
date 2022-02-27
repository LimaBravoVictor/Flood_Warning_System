
"""Submodule used for creating plots of monitoring station data:"""

from pyrsistent import b
from floodsystem.station import MonitoringStation
import matplotlib.pyplot as plt
import matplotlib.dates as dt
from floodsystem.analysis import polyfit
import numpy as np
import datetime


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
    for i in range(0, len(dates)):
        list.append(low)
    plt.plot(dates, list, '--', color='g',)
    list = []
    for i in range(0, len(dates)):
        list.append(high)
    plt.plot(dates, list, '--', color='g')


def plot_water_levels(station, dates, levels):
    """Plots water levlels at a Station, where station is a monitoring station object;
    dates are a list of sorted dates
    levels are a corresponding list of levels"""
    if station.typical_range_consistent:
        plot_high_low(dates, station.typical_range[0], station.typical_range[1])
    plt.plot(dates, levels, color='b')
    lables_and_title(station.name)
    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p, high_low=False):
    """Plots water levlels at a Station, where station is a monitoring station object;
    dates are a list of sorted dates
    levels are a corresponding list of levels
    Also ploys the polynomial line of best fit to degree p"""
    plt.clf()
    if station.typical_range_consistent and True:
        plot_high_low(dates, station.typical_range[0], station.typical_range[1])

    plt.plot(dates, levels, 'b')

    polyline, start = polyfit(dates, levels, p)
    poly = np.poly1d(polyline)
    num_dates = []
    for i in dates:
        num_dates.append(dt.date2num((i - start) / datetime.timedelta(microseconds=1)))
    # Evalute
    polylevels = []
    for i in num_dates:
        polylevels.append(poly(i))
    plt.plot(dates, polylevels, 'r')
    # Lables
    lables_and_title(station.name)
    plt.tight_layout()
    plt.show()
