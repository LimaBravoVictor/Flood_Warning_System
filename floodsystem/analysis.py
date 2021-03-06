"""Module for analysing station data"""

from ast import Import


import matplotlib.dates as dt
import numpy as np
import datetime

from floodsystem.station import MonitoringStation

def polyfit(dates, levels, p):
    """From a list of dates and levels returns a best fit numpy polynomial of order p, 
    and the shift of the date axis as a datetime object"""
    if len(dates)<2 or len(dates)!=len(levels):
        raise ValueError("Input invalid")
    lowest_date = dates[-1]
    #Use datetime function to deduct the lowest date:
    delta_dates =[]
    for d in dates:
        delta_dates.append(d - lowest_date)
    #Then convert to floats, reducing floating point errors:
    float_dates =[]
    for i in delta_dates:
        float_dates.append((dt.date2num(i/datetime.timedelta(microseconds=1))))
        #dividing by microsceconds=1 converts timedelta back into datetime
    polyline = np.poly1d(np.polyfit(np.array(float_dates),np.array(levels), p))
    return polyline, lowest_date

def gradient(dates, levels):
    """Returns the gradient of the line of regression plotted for dates levels (m/day)"""
    try: line, date = polyfit(dates,levels, 1)
    except ValueError: 
        raise ValueError("Gradient could not be calculated")
    #since gradiant constant, does not matter when we take derivative
    grad = line.deriv(1)
    return float(grad(1))