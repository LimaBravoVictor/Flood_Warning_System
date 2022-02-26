"""Module for analysing station data"""

from ast import Import


import matplotlib.dates as dt
import numpy as np
import datetime
from floodsystem.station import MonitoringStation

def polyfit(dates, levels, p):
    """From a list of dates and levels returns a best fit numpy polynomial of order p, 
    and the shift of the date axis as a datetime object"""
    lowest_date = dates[-1]
    #Use datetime function to deduct the lowest date:
    delta_dates =[]
    for d in dates:
        delta_dates.append(d - lowest_date)
    #Then convert to floats, reducing floating point errors:
    float_dates =[]
    for i in delta_dates:
        float_dates.append((dt.date2num(i/datetime.timedelta(microseconds=1))))
        #dividing by days =1 converts timedelta back into datetime
    polyline = np.polyfit(np.array(float_dates),np.array(levels), p)
    return polyline, lowest_date
