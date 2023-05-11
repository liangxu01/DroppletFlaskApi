from classes.IntializeData import *
import json

"""
Given a list of all buildings sorted by how close they are in feet to the cords we provided
"""
def nearestBuilding(buildingList, cords):

    distanceMap = {}

    for building in buildingList:
        buildingCords = building.cords
        distance = cords.distance(buildingCords)
        distanceMap[building] = distance
    
    sortedMap = sorted(distanceMap.items(), key=lambda x:x[1])

    return sortedMap
    
def print5buildings(list): 

    finalReturn = {}
    finalReturn['places'] = []

    allBuildings = []

    for i in range(0, 5):
        buildingTuple = list[i]
        
        buildingObject = buildingTuple[0]
        distance = buildingTuple[1]
        cords = buildingObject.cords

        buildName = buildingObject.buildingName
        stationList = buildingObject.stationList
        buildingID = buildingObject.buildingID

        print(buildName, distance, 'ft')

        stationDictList = [] 
        
        for station in stationList:

            stationDict = {}

            stationID = station.stationID
            floor = station.floor 
            status = station.status
            notes = station.notes

            stationDict = {"stationID": stationID, "floor": floor, "status": status, "notes": notes}
            stationDictList.append(stationDict)
        
        lat = cords.lat  
        lon = cords.lon
        buildingDict = {"buildingName": buildName, "lat": lat, "lon": lon, "stationList": stationDictList}
        allBuildings.append(buildingDict)
    
    finalReturn['places'] = allBuildings

    return json.dumps(finalReturn)

def createReport(lat, lon):
    #Creates the Different Buildings According to CSV: 
    buildingList = IntializeBuildings("Data/building.csv")

    #Appends the Water Stations Into the Building Data Structure: 
    IntializeStations(buildingList, "Data/station.csv")

    cords = Coordinates(lat, lon)
    closestBuilding = nearestBuilding(buildingList, cords)
    return  print5buildings(closestBuilding)


def main():

    report = createReport(42.393433, -72.525697)

if __name__ == "__main__":
    main()