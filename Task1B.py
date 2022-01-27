#Luke Vogt

import floodsystem.station as station
import floodsystem.stationdata as data
import floodsystem.geo as geo

centre = (52.2053, 0.1218)

def run():
    station_list = data.build_station_list()
    #Find distances
    distance_list = geo.stations_by_distance(station_list, centre)
    closest = distance_list[:10]
    futhest = distance_list[-10:]
    print(closest)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
