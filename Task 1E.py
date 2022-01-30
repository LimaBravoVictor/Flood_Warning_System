# Songha Kim
from floodsystem.stationdata import build_station_list
import floodsystem.station as station
from floodsystem.geo import rivers_by_station_number


def run():
    print("List of stations (river, number stations) tuples when N = 9:")
    stations = build_station_list()
    river_number_list = rivers_by_station_number(stations, 9)
    print(river_number_list)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
