"""List the town  where you assess the risk of flooding to be greatest.
Explain the criteria that you have used in making your assessment
and rate the risk at severe/high/moderate/low."""


from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import level_next_day
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import gradient
from floodsystem.geo import towns_with_station


def town_extra_water(town_list=[]):
    """Returns a list of town, extrawater tuples for a list of town names
    extrawater being water above typical range"""
    retlist = []
    stations = build_station_list()
    update_water_levels(stations)
    for town in town_list:
        town_risk = -10000000.0
        for station in stations:
            if station.town == town:
                if (station.typical_range is not None) and station.typical_range_consistent():
                    l = -10000
                    # predicted absolute level
                    try:
                        l = level_next_day(station)
                    except ValueError:
                        l = -10000
                    # difference between predicted absolute level and current typical high level
                    l = l - (station.typical_range[1])
                    if l > town_risk:
                        # town risk = absolute level (l)
                        town_risk = l
        retlist.append((town, town_risk))
    return retlist


def select_one_station(stations):
    # select one station that has highest gradient
    update_water_levels(stations)

    st_with_predicted_level = []

    # comparing each station to find the station that gives highest level and remove the rest.
    for station1 in stations:
        level_next_day1 = level_next_day(station1)
        for station2 in stations:
            level_next_day2 = level_next_day(station2)
            if level_next_day1 >= level_next_day2:
                st_with_predicted_level.append((station1.town, level_next_day1))
        return st_with_predicted_level


def risk_cat(risk):
    """Returns the catagory of risk based on risk"""
    if risk < 0.0:
        return "Low"
    elif risk < 0.5:
        return "Moderate"
    elif risk < 2:
        return "High"
    elif risk < 100000000:
        return "Severe"
    else:
        return "Could not be calculated"


def run():
    stations = build_station_list()
    update_water_levels(stations)
    write_to_file = True
    if write_to_file:
        f = open("one_I_prepared_earlier.txt", "a")
        f.write("Station, risk , expected, level")
    # severe : town risk < 100000000
    # high : town risk <2
    # moderate : town risk < 0.5
    # low : town risk < 0

    names = [
        'Cambridge', 'Swindon'
    ]
    names = towns_with_station(stations)
    l = town_extra_water(names)
    a = sorted(l, key=lambda kv: kv[1], reverse=True)

    for level in a:
        message = risk_cat(level[1])
        if write_to_file:
            f.write("\n{} is {} at {}".format(level[0], message, round(level[1], 5)))
        print("{} is {} at {}".format(level[0], message, round(level[1], 5)))
    if write_to_file:
        f.close


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
