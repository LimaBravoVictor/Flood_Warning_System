from floodsystem.station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    """
    a list of tuples (station object at which latest relative water level is 
    over tol, the relative water level at the station)
    returned list is sorted by the relative level in descending order
    """
    station_list = []
    relative_level_list = []
    for station in stations:
        if station.typical_range:
            relative_level = station.relative_water_level()
            if relative_level > tol:
                station_list.append(station)
                relative_level_list.append(relative_level)

    station_and_relative_level = list(zip(station_list, relative_level_list))
    station_and_relative_level.sort(key=lambda item: item[1], reverse=True)

    return station_and_relative_level
