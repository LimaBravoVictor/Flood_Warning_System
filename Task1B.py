#Luke Vogt

from unicodedata import name
import floodsystem.station as station
import floodsystem.stationdata as data
import floodsystem.geo as geo

centre = (52.2053, 0.1218)

def run():
    station_list = data.build_station_list()
    #Find distances
    distance_list = geo.stations_by_distance(station_list, centre) #Already ordered
    format_list = []
    for group in distance_list:
        format_list.append((group[0].name , group[0].town ,group[1]))
        # This gives the same order as distancelist
    #Slice list
    close = format_list[:10]
    far = format_list[-10:] 
    print ("These are the 10 closest stations to Cambridge city centre:")
    print(close)
    print ("These are the 10 furthest stations to Cambridge city centre:")
    print(far)    


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
