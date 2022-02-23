# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from ast import Import


import floodsystem.station as station


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_relative_water_level():
    test_list = [(None, None),(1,0),(2,1),(1.2,0.2),(3.5, 2.5), (0, -1)]
    #Create a station 
    trange = (1.0, 2.0)
    test_st = station.MonitoringStation("s_id", "m_id", "label", (0.0,0,0), trange, "Ryn", "Rynmouth")
    #Add and try various water levels:
    for i in test_list:
        test_st.latest_level = i[0]
        output = test_st.relative_water_level()
        if i[0] is None:
            assert output is None
        else:
            assert round(output, 2) == i[1]
