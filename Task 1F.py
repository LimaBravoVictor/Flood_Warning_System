# Songha Kim

from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    print("List of station names, in alphabetical order, for stations with inconsistent data: ")
    stations = build_station_list()

    # list of stations with inconsistent range data
    inconsistent_data = inconsistent_typical_range_stations(stations)

    station_name = []
    for station in inconsistent_data:
        station_name.append(station.name)

    # Put into alphabetical order:
    station_name.sort()
    print(station_name)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
