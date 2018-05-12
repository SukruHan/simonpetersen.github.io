import csv
import json
from shapely.geometry import shape, Point

file = open('../data/NycVehicleCollisions2017.csv')
newFile = open('../data/NycVehicleCollisions2017_geo-1.csv', 'w')
json = json.load(open('../data/boroughs.json'))
reader = csv.reader(file)

newFile.write('date,hour,borough,seriousDegree,taxi,pedestrianCyclist,vehicles,uniqueKey')

for row in reader:
    borough = row[2]
    lat = row[8]
    lon = row[9]
    if borough == '' and lat != '' and lon != '' and lat != 'lat':
        point = Point(float(lon),float(lat))
        # Check in boroughs.json, if coordinates is inside one of the boroughs
        for feature in json['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                borough = feature['properties']['BoroName']
                break
        # If empty, the borough can't be determined.
        if borough == '':
            borough = 'Unknown'
    
    # Write to file
    newRow = row[0] + ',' + row[1] + ',' + borough + ',' + row[3] + ',' + row[4] + ',' + row[5] + ','
    newRow += row[6] + ',' + row[7]
    newFile.write('\n')
    newFile.write(newRow)

file.close()
newFile.close()