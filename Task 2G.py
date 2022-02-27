"""List the town  where you assess the risk of flooding to be greatest.
Explain the criteria that you have used in making your assessment
and rate the risk at severe/high/moderate/low."""


from floodsystem.stationdata import build_station_list
from floodsystem.flood import flood_risk_rate
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import gradient
import datetime


def run():
    stations = build_station_list()

    # severe : relative water level > 2 and gradient > 0.3
    # high : relative water level > 1 and gradient > 0.1
    # moderate : relative water level < 1 and gradient > 0
    # low : else
    severe_station = stations_level_over_threshold(stations, 2)
    severe_town = []

    for st in severe_station:
        dates, levels = fetch_measure_levels(st[0].measure_id, datetime.timedelta(1))
        # water level increases more than 0.3m/day
        try:
            gradient(dates, levels)
        except ValueError:

        if gradient(dates, levels) >= 0.3:
            severe_town.append(st.town)
        return severe_town

    print("{}: severe".format(severe_town))


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
