import csv
import numpy

oldFile = open('/Users/Simon/Documents/NYPD_Complaint_Data_Historic.csv')
newFile = open('Crime-Data.csv', 'w')
readerOldFile = csv.reader(oldFile)

newFile.write('Hour,Lat,Lon')

# Read values of csv-file.
for row in readerOldFile:
        ofnsDesc = row[7]
        date = row[1]
        year = date[-4:]
        if ofnsDesc != 'OFNS_DESC' and 'MURDER' in ofnsDesc and year == '2016':
            lat = row[21]
            lon = row[22]
            if lat != '' and lon != '':
                time = row[2]
                hour = time[:2]
                if hour[0] == '0':
                    hour = hour[1]
                row = hour + "," + lat + "," + lon
                newFile.write("\n")
                newFile.write(row)

oldFile.close()
newFile.close()