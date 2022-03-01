"""Unit test for the flood module"""

from tkinter.tix import StdButtonBox
from sklearn.preprocessing import StandardScaler
import floodsystem.flood
from floodsystem.station import MonitoringStation

def test_stations_over_threshold():
    StA = MonitoringStation("01","2","Bob",(1,1), (0, 1), "Humber", "town")