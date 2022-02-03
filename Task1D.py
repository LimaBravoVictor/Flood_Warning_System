# Luke Vogt

import floodsystem.station as station
import floodsystem.stationdata as data
import floodsystem.geo as geo

rivers_of_intrest = ["River Aire", "River Cam", "River Thames", ]


def run():
    print("Number of rivers with at least one monitoring station:")
    # At least one == one ore more
    station_list = data.build_station_list()
    rivers = sorted(geo.rivers_with_station(station_list))
    print("{} stations. - First 10 - {}".format(len(rivers), rivers[:10]))

    by_river = geo.stations_by_river(station_list)
    for river in rivers_of_intrest:
        print("\nStations on the river " + river)
        # Get names
        names = [r.name for r in by_river[river]]
        print(sorted(names))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
