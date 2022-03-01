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
    """
    return a list of (river name, number of stations) tuples, 
    sorted by the number of stations. In the case that there are more rivers 
    with the same number of stations as the N th entry, include these rivers in the list
    """
    station_num = {}
    for s in stations:
        if s.river in station_num:
            station_num[s.river] += 1
        else:
            station_num[s.river] = 1

    river_station_num = sorted(station_num.items(), key=lambda kv: kv[1], reverse=True)
    working_list = river_station_num[N:]
    output_list = river_station_num[0:N]
    for river in working_list:
        if river[1] == output_list[- 1][1]:
            output_list.append(river)

    return output_list

def towns_with_station(stations):
    """Returns a set of towns witch have stations"""
    towns = set()
    for station in stations:
        if station.town is not None:
            towns.add(station.town)
    return(sorted(towns))
