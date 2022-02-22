"""Module for analysing station data"""

from matplotlib import dates
import numpy as np
import datetime
from .station import MonitoringStation

def polyfit(dates, levels, p):
    """From a list of dates and levels returns a best fit numpy polynomial of order p, and the shift of the date axis"""
    lastdate= dates[:-1]