# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from haversine import haversine, Unit

from floodsystem.stationdata import build_station_list

from floodsystem.station import MonitoringStation


def stations_by_distance(stations, p):

    stations = build_station_list()

    station_name = [stations.name for station in stations]
    distance = list(haversine(stations.coord, p))

    # a list of (station, distance) tuples
    stations_distance = list(zip(station_name, distance))

    # list sorted by distance
    return sorted_by_key(stations_distance, 1)

def stations_within_radius(stations, centre, r):
    """
    From a list of MonitoringStation() objects, 
    returns a new list of station MonitoringStation() objects 
    which lie less then r from centre
    """
    close_stations = []
    for s in stations:
        d = haversine(s.coord, centre)
        if d < r:
            close_stations.append(s)
    return close_stations



def rivers_with_station(stations):
    """
    For a list of MonitoringStation() objects, returns a set of rivers that those stations lie on
    """
    rivers ={}
    for s in stations:
        rivers.add(s.river)
    return rivers



