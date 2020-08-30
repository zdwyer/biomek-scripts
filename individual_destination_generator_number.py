#! C:\Python\Python38\python.exe

import sys, math, os
from collections import defaultdict

# Remove old load files as a failsafe to prevent Biomek from starting to pool if API call fails (as it might use previous load files)
if os.path.exists("C:\cu-beckman\csv_files\individual\individual.csv"):
	os.remove("C:\cu-beckman\csv_files\individual\individual.csv")

storage_key =  {1:"1A", 2:"1B", 3:"1C", 4:"1D", 5:"1E", 6:"1F"}

output = []

num_samples = int(sys.argv[1])
identifier = sys.argv[2]

for sample in range(min(num_samples, 93)):
	TS = math.floor(sample / 16)
	position = sample % 16
	row = chr(sample % 8 + 65)
	column = math.floor(sample / 8)
	output.append((sample, TS, position, row, column))	

with open("C:\cu-beckman\csv_files\individual\individual.csv", 'w') as out:
	out.write("Source,Source_Well,Destination,Destination_Well\n")
	out.write('\n'.join(['%s,%d,%s,%s%d' % (storage_key[i[1]+1], i[2]+1, identifier, i[3], i[4]+1) for i in output]))

print(num_samples, end='')