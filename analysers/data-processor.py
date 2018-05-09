import csv
import numpy

oldFile = open('../data/NYPD_Motor_Vehicle_Collisions.csv')
newFile = open('../data/NycVehicleCollisions_all.csv', 'w')
readerOldFile = csv.reader(oldFile)

newFile.write('date,hour,borough,seriousDegree,taxi,pedestrianCyclist,vehicles,uniqueKey')

def getNumberOfVehicles(vehicleString):
    if vehicleString != '':
        return 0
    return vehicleString.count('+') + 1

def isTaxiInvolved(vehicleTypes):
    if vehicleTypes is not None:
        return 'TAXI' in vehicleTypes
    return False

def getHourValue(time):
    hour = time[:2]
    if (hour[1] == ':'):
        return hour[0]
    return hour[:2]

# 1 = No injuries or fatalities, 2 = Injuries but no fatalities, 3 = Fatal
def getSeriousDegree(injured,killed):
    if killed > 0:
        return 3
    if injured > 0:
        return 2
    return 1

# Combining five rows. Used for vehicle types and contributing factors
def concatFiveValues(row, i):
    if row[i] == 'Unspecified':
        return ''
    j = i + 1
    values = row[i]
    while j < i + 5:
        if row[j] == '' or row[j] == 'Unspecified':
            return values
        else:
            values += '+' + row[j]
            j = j + 1

# Read values of csv-file.
for row in readerOldFile:
        date = row[0]
        year = date[-4:]
        #if year == '2017':
        if date != 'DATE':
            lat = row[4]
            lon = row[5]
            time = row[1]
            hour = getHourValue(time)
            factors = concatFiveValues(row,18)
            vehicleTypes = concatFiveValues(row,24)
            taxi = isTaxiInvolved(vehicleTypes)
            degree = getSeriousDegree(int(row[10]), int(row[11]))
            pedestrianCyclistInvolved = int(row[12]) > 0 or int(row[13]) > 0 or int(row[14]) > 0 or int(row[15]) > 0
            borough = row[2]
            vehicles = getNumberOfVehicles(vehicleTypes)
            # Add values to row. Column 23 is UniqueKey
            newRow = date + ',' + hour + ',' + borough + ',' + str(degree) + ',' + str(taxi) + ','
            newRow += str(pedestrianCyclistInvolved) + ',' + str(vehicles) + ',' + row[23]
            newFile.write('\n')
            newFile.write(newRow)

oldFile.close()
newFile.close()