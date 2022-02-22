
"""Submodule used for creating plots of monitoring station data:"""

from floodsystem.station import  MonitoringStation
import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    """Plots water levlels at a Station, where station is a monitoring station object;
    dates are alist of dates
    levels are a corresponding list of levels"""

    plt.plot(dates, levels)
    #Plot low and high
    if station.typical_range_consistent:
        list = []
        for i in range (0, len(dates)):
            list.append(station.typical_range[0])
        plt.plot(dates, list)
        list = []
        for i in range (0, len(dates)):
            list.append(station.typical_range[1])
        plt.plot(dates, list)
    # Lables
    plt.xlabel("Date (YYYY-MM-DD)")
    plt.ylabel("Water Level (m)")
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()
