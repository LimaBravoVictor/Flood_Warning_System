"""Module for analysing station data"""

from matplotlib import dates
import numpy as np
import datetime
from .station import MonitoringStation

def polyfit(dates, levels, p):
    """From a list of dates and levels returns a best fit numpy polynomial of order p, 
    and the shift of the date axis as a datetime object"""
    if dates[0] < dates [-1]:
        lowest_date = dates[0]
    else:
        lowest_date = dates[-1]
    #Use datetime function to deduct the lowest date:
    delta_dates =[]
    for d in dates:
        delta_dates.append(d - lowest_date)
    #Then convert to floats, reducing floating point errors:
    float_dates = dates.date2num(delta_dates)
    polyline = np.polyfit(np.array(float_dates),np.array(levels), p)
    return polyline, lowest_date
