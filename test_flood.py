"""Unit test for the flood module"""

from tkinter.tix import StdButtonBox
from sklearn.preprocessing import StandardScaler
import floodsystem.flood as flood
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():
    sta = MonitoringStation("01","2","Bob",(1,1), (0, 1), "Humber", "town")
    sta.latest_level = 0
    stb = sta
    stb.latest_level =1
    stc =sta
    stc.latest_level =2
    list = (sta, stb, stc)
    st_list = flood.stations_level_over_threshold(list, 1)
    assert (stc, 1) in st_list
    