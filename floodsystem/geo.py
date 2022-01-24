# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from haversine import haversine, Unit

from floodsystem.stationdata import build_station_list

from station import MonitoringStation


def stations_by_distance(stations, p):

    stations = build_station_list()

    station_name = [stations.name for station in stations]
    distance = list(haversine(stations.coord, p))

    # a list of (station, distance) tuples
    stations_distance = list(zip(station_name, distance))

    # list sorted by distance
    return sorted_by_key(stations_distance, 1)
