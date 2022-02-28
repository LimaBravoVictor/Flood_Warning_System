"""List the town  where you assess the risk of flooding to be greatest.
Explain the criteria that you have used in making your assessment
and rate the risk at severe/high/moderate/low."""


from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import level_next_day
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import gradient
import datetime

def town_extra_water(town_list=[]):
    """Returns a list of town, extrawater tuples for a list of town names
    extrawater being water above typical range"""
    retlist=[]
    stations = build_station_list()
    update_water_levels(stations)
    for town in town_list:
        town_risk = -10000000.0
        for station in stations:
            if station.town == town:
                l = -10000
                try:
                    l = level_next_day(station)
                except ValueError:
                    l = -10000
                l = l - (station.typical_range[1])
                if l > town_risk:
                    town_risk =l
        retlist.append((town, town_risk))
    return retlist

def risk_cat(risk):
    """Returns the catagory of risk based on risk"""
    if risk < -0.5:
        return "Low"
    elif risk < 0.2:
        return "Moderate"
    elif risk < 100:
        return "Severe"
    else:
        return "Could not be calculated"

def run():
    stations = build_station_list()
    update_water_levels(stations)

    # severe : relative water level > 2 and gradient > 0.3
    # high : relative water level > 1 and gradient > 0.1
    # moderate : relative water level < 1 and gradient > 0
    # low : else

    names = [
        'Cambridge','Swindon'
    ]
    l = town_extra_water(names)
    print (l)
    


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
