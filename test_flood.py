"""Unit test for the flood module"""

from tkinter.tix import StdButtonBox
import floodsystem.flood as flood
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level


def test_stations_level_over_threshold():
    sta = MonitoringStation("01", "2", "Bob", (1, 1), (0, 1), "Humber", "town")
    sta.latest_level = 0
    stb = sta
    stb.latest_level = 1
    stc = sta
    stc.latest_level = 2
    list = (sta, stb, stc)
    st_list = flood.stations_level_over_threshold(list, 1)
    assert (stc, 1) in st_list


def test_stations_highest_rel_level():
    # create list of test stations
    sta = MonitoringStation("stid", "mid", "name", (1, 1), (0, 1), "river", "town")
    sta.latest_level = 5

    stb = sta
    stb.latest_level = 10

    stc = sta
    stc.latest_level = 20

    std = sta
    std.latest_level = None

    test_station_list = [sta, stb, stc, std]

    result = stations_highest_rel_level(test_station_list, 3)

    assert result[0] == stc
    assert result[1] == stb
    assert result[2] == sta


test_stations_highest_rel_level()
