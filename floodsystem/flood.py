from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels
from floodsystem.analysis import gradient
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def stations_level_over_threshold(stations, tol):
    """
    a list of tuples (station object at which latest relative water level is 
    over tol, the relative water level at the station)
    returned list is sorted by the relative level in descending order
    """
    station_list = []
    update_water_levels(stations)

    for station in stations:
        if station.latest_level:
            relative_level = station.relative_water_level()
            if relative_level and relative_level > tol:
                station_list.append((station, relative_level))

    station_list.sort(key=lambda item: item[1], reverse=True)

    return station_list


def stations_highest_rel_level(stations, N):
    """
    Returns a list of the N stations (objects) at which the water level, 
    relative to the typical range, is highest.
    Sorted in descending order by relative level
    """

    update_water_levels(stations)

    station_list = []
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level is not None:
            station_list.append((station))

    station_list.sort(key=lambda item: item.relative_water_level(), reverse=True)
    highest_water_level = station_list[:N]

    return highest_water_level


def flood_risk_rate(stations, no_days =1):
    """ 
    Calculating risk coefficient of each station for previous dates, using regression over the past no_days
    to calculate gradient. If no gradient can be calculated, the relative level is returned instead
    """
    update_water_levels(stations)
    # list of tuples (station, risk coeff)
    station_with_risk_coeff = []
    for station in stations:
        dates , levels = dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(no_days))
        try: grad =gradient(dates, levels)
        except ValueError:
            grad = 0
            
        if not station.typical_range_consistent or (station.relative_water_level() is None):
            risk_coeff = None
        else:
            risk_coeff = float(station.relative_water_level() - grad)
        station_with_risk_coeff.append((station, risk_coeff))
    return station_with_risk_coeff
