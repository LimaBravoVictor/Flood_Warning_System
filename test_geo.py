"""Unit test for the geo module"""

import string

from sqlalchemy import null
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
    output = geo.stations_by_distance(stationlist, point)
    #Check Types
    assert type(output) == list
    assert type(output[0])== tuple
    assert isinstance (station.MonitoringStation(), output[0][0])
    #Check Values
    assert output[0][0].name == "Station2"
    assert output[1][0].name == "Station3"
    assert output[2][0].name == "Station1"
    assert round(output[0][1]-d2, 3)==0
    assert round(output[1][1]-d3, 3)==0
    assert round(output[2][1]-d1, 3)==0

def test_rivers_by_station_number():
    #create list of test rivers:
    test_rivers =[]
    for i in range (1, 101):
        test_rivers.append(("River{}".format(i), i))
    #Create empty stationlist:
    station_list=[]
    #Create stations on those rivers
    for i in test_rivers:
        for j in range( i[1]):
            sid = "sid{},{}".format(i[0], j)
            mid = "md{},{}".format(i[0], j)
            name = "name{},{}".format(i[0], j)
            coord = (j, -j)
            trange = (-j,j)
            town ="town{},{}".format(i[0], j)
            station_list.append(station.MonitoringStation(sid,mid, name, coord, trange, i[0], town))
    
    #Test Lengths
    for i in range(1, 100):
        output = geo.rivers_by_station_number(station_list, i)        
        assert len(output) == i
    #Test type returns
    output = geo.rivers_by_station_number(station_list, 10)
    assert type(output)== list
    assert type(output[0])== tuple
    assert type(output[0][0])== string
    assert type(output[0][1])== int
    #Value checks
    assert output[0][0] == "River100"
    assert output[9][0] == "River90"
    assert output[0][1] == 100
    assert output[9][1] == 90

def test_typical_range_consistent():
    #Create and test consistant stations
    for i in range (-100, 100):
        sid = "sid{}".format(i)
        mid = "md{}".format(i)
        name = "name{}".format(i)
        coord = (1, 3)
        trange = (i,i+1)
        town ="town{}".format(i)
        s=station.MonitoringStation(sid,mid, name, coord, trange, i, town)
        assert s.typical_range_consistent()
    #Create and test inconsistant station
    incon = station.MonitoringStation("01","01","Constistant", (2,1),(2,1), "bob", "Cannon" )
    assert incon.typical_range_consistent() == False
    #Test no data
    no_data = station.MonitoringStation("01","01","Constistant", (1,1),"n/a" ,"bob", "Cannon" )
    assert no_data.typical_range_consistent() == False
    none_data = station.MonitoringStation("01","01","Constistant", (1,1), None ,"bob", "Cannon" )
    assert none_data.typical_range_consistent() == False

def test_inconsistent_typical_range_stations():
    #Create stations
    none_data = station.MonitoringStation("01","01","none", (1,1), None ,"bob", "Cannon" )
    incon = station.MonitoringStation("01","01","incon", (2,1),(2,1), "bob", "Cannon" )
    stationlist = [none_data, incon]
    for i in range (-100, 100):
        sid = "sid{}".format(i)
        mid = "md{}".format(i)
        name = "name{}".format(i)
        coord = (1, 3)
        trange = (i,i+1)
        town ="town{}".format(i)
        stationlist.append(station.MonitoringStation(sid,mid, name, coord, trange, i, town))
    output = station.inconsistent_typical_range_stations(stationlist)
    assert type(output) == list
    for i in output:
        assert isinstance(i, station.MonitoringStation)
        pass
    assert len(output)==2
test_inconsistent_typical_range_stations()