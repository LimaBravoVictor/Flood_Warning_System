
"""Submodule used for creating plots of monitoring station data:"""

import floodsystem.station as station
from  datetime import datetime, timedelta
import matplotlib as plt

def plot_water_levels(station, dates, levels):
    """Station is a monitoring station object
    Dates (tuple of datetime tupes(Year, mounth, day)) define beteen which dates
    """