#Luke Vogt

import floodsystem.station as station
import floodsystem.stationdata as data
import floodsystem.geo as geo

centre = (52.2053, 0.1218)
radius = 10

def run():
    
    station_list = data.build_station_list()
    #List of stations within radius
    within_radius = geo.stations_within_radius(station_list, centre, radius)
    #Put names in list
    names = []
    for station in within_radius:
        names.append(station.name)
    #Put into alphabetical order:
    names.sort()
    print(names)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
