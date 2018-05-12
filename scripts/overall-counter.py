import csv
import numpy
import datetime

oldFile = open('../data/NYPD_Motor_Vehicle_Collisions.csv')
newFile = open('../data/NycOverallCount.csv', 'w')
readerOldFile = csv.reader(oldFile)

newFile.write('date,simple,serious,fatal,total')

counter = {}

def getSeriousDegree(injured,killed):
    if killed > 0:
        return 3
    if injured > 0:
        return 2
    return 1

# Read through values and count number of accidents each day.
for row in readerOldFile:
        date = row[0]
        if date != 'DATE':
            # Get degree of accident based on number of injured (10) and kills (11)
            degree = getSeriousDegree(int(row[10]), int(row[11]))
            if date not in counter:
                counter[date] = [0, 0, 0]
            counter[date][degree-1] = counter[date][degree-1] + 1

oldFile.close()

keys = counter.keys()
keys.sort(key=lambda k: datetime.datetime.strptime(k, '%m/%d/%Y'))
for key in keys:
    total = counter[key][0] + counter[key][1] + counter[key][2]
    newFile.write('\n')
    row = key + ',' + str(counter[key][0]) + ',' + str(counter[key][1]) + ',' + str(counter[key][2]) + ',' + str(total)
    newFile.write(row)

newFile.close()