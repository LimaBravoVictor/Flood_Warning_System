"""List the town  where you assess the risk of flooding to be greatest.
Explain the criteria that you have used in making your assessment
and rate the risk at severe/high/moderate/low."""


from floodsystem.stationdata import build_station_list
from floodsystem.flood import flood_risk_rate
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import floodsystem.plot as plot


def run():
    stations = build_station_list()

    # risk coefficient for each station (give list of tuples (station, risk coeff))
    station_risk_coeff = flood_risk_rate(stations)

    # select the highest risk coeff for the town that has multiple stations.
    for st in station_risk_coeff:
        if st[0].town in station_risk_coeff[:][0].town
