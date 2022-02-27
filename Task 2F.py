# Luke Vogt

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import floodsystem.plot as plot

no_stations = 5
no_Days = 2
polyfit = 4


def run():
    stations = build_station_list()
    highlevel = stations_highest_rel_level(stations, no_stations)
    for st in highlevel:
        dates, levels = fetch_measure_levels(st.measure_id, datetime.timedelta(no_Days))
        plot.plot_water_level_with_fit(st, dates, levels, polyfit)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
