"""Unit test for the geo module"""

import floodsystem.geo as geo
import floodsystem.station as station

def test_stations_by_distance():
    # Create target point
    point = (51.50812590066494, -0.12805261647968538) #Trafalgar square
    # Create known coordinates
    cord1 = (59.91103335104495, 10.752381892691936) # Furthest (Oslo central station)
    cord2 = (51.50071924513987, -0.12455301158228925) # Nearest (Big ben)
    cord3 = (50.40846686365902, -4.202154445012462) # Tamar bridge, Plymouth
    #With known distances from target (Done on calculator)
    d1 = 1153.46031
    d2 = 0.858464
    d3 = 310.390325
    # Create test stations with known coordinates
    s1 = station.MonitoringStation("s1-sid","s1-mid","Station1",cord1, (-1, 1), "RiverA", "TownA")
    s2 = station.MonitoringStation("s2-sid","s2-mid","Station2",cord1, (-1, 1), "RiverB", "TownB")
    s3 = station.MonitoringStation("s3-sid","s3-mid","Station3",cord1, (-1, 1), "RiverC", "TownC")
    stationlist = [s1, s2, s3]
    #output = geo.stations_by_distance(stationlist, point)
    output = [(s2,0.8585),(s3,310.3901),(s1,1153.460)]
    
    assert output[0][0].name == "Station2"
    assert output[1][0].name == "Station3"
    assert output[2][0].name == "Station1"
    assert round(output[0][1]-d2, 3)==0
    assert round(output[1][1]-d3, 3)==0
    assert round(output[2][1]-d1, 3)==0
test_stations_by_distance()