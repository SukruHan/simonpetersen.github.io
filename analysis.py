import csv
import numpy as np

file = open('data/pres.csv')
reader = csv.reader(file)
numberOfBins = 8
values = []

# Read values of csv-file into array.
for row in reader:
    value = row[1]
    if (value != 'days'):
        values.append(int(row[1]))

file.close()

# Create histogram bins with numpy.histogram.
bins = np.histogram(values, numberOfBins)

# Write histogram-data to new csv-file.
file = open('data/pres-bins.csv', "w")
file.write('x0,x1,count\n')
for i in range(0, len(bins[0])):
    file.write("{},{},{}\n".format(bins[1][i], bins[1][i+1], bins[0][i]))

file.close()