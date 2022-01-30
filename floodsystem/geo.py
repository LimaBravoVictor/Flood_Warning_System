# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from haversine import haversine, Unit

from .stationdata import build_station_list

from .station import MonitoringStation


def stations_by_distance(stations, p):

    distance = {}
    for s in stations:
        d = haversine(s.coord, p)
        distance[s] = d

    # a list of (station, distance) tuples
    stations_distance = distance.items()

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
    rivers = set()
    for s in stations:
        rivers.add(s.river)
    return rivers


def stations_by_river(stations):
    """
    From a list of MonitoringStation() objects, 
    returns a dictionary with keys corresponding to names of rivers
    with each value being a list of MonitoringStation() stations that are on the river
    """
    by_river = dict()
    # Get a list o keys and create empty dictionary
    key_list = rivers_with_station(stations)
    for river in key_list:
        by_river[river] = []
    # Add stations to rivers
    for station in stations:
        by_river[station.river].append(station)
    return by_river


def rivers_by_station_number(stations, N):
    station_num = {}
    for s in stations:
        if s.river in station_num:
            station_num[s.river] += 1
        else:
            station_num[s.river] = 1

    river_station_num = sorted(station_num.items(), key=lambda kv: kv[1], reverse=True)

    return river_station_num[0:N]
