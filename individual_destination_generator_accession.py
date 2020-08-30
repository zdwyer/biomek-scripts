#! C:\Python\Python38\python.exe

import sys, math, json, os
from collections import defaultdict
from urllib.request import urlopen

if os.path.exists("C:\cu-beckman\csv_files\individual\individual.csv"):
	os.remove("C:\cu-beckman\csv_files\individual\individual.csv")


storage_key =  {1:"1A", 2:"1B", 3:"1C", 4:"1D", 5:"1E", 6:"1F"}

output = []

accession = sys.argv[1]
with urlopen("https://public-api.vmit.cucloud.net/vetview_api_19/accession_covid_item_count/%s" % (accession)) as response:
	response_content = response.read()
json_response = json.loads(response_content)

num_samples = json_response['items']

for sample in range(min(num_samples, 93)):
	TS = math.floor(sample / 16)
	position = sample % 16
	row = chr(sample % 8 + 65)
	column = math.floor(sample / 8)
	output.append((sample, TS, position, row, column))	

with open("C:\cu-beckman\csv_files\individual\individual.csv", 'w') as out:
	out.write("Source,Source_Well,Destination,Destination_Well\n")
	out.write('\n'.join(['%s,%d,Individual_Plate,%s%d' % (storage_key[i[1]+1], i[2]+1, i[3], i[4]+1) for i in output]))

print(num_samples, end='')