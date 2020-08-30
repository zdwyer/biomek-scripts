#! C:\Python\Python38\python.exe

import sys, math, json, os
from collections import defaultdict
from urllib.request import urlopen

# Remove old load files as a failsafe to prevent Biomek from starting to pool if API call fails (as it might use previous load files)
if os.path.exists("C:\cu-beckman\csv_files\pooling\pooling_load1.csv"):
	os.remove("C:\cu-beckman\csv_files\pooling\pooling_load1.csv")
if os.path.exists("C:\cu-beckman\csv_files\pooling\pooling_load2.csv"):
	os.remove("C:\cu-beckman\csv_files\pooling\pooling_load2.csv")
if os.path.exists("C:\cu-beckman\csv_files\pooling\pooling_load3.csv"):
	os.remove("C:\cu-beckman\csv_files\pooling\pooling_load3.csv")

storage_key =  {1:"1A", 2:"1B", 3:"1C", 4:"1D", 5:"1E", 6:"1F", 7:"2A", 8:"2B", 9:"2C", 10:"2D", 11:"2E", 12:"2F", 13:"3A", 14:"3B", 15:"3C", 16:"3D", 17:"3E", 18:"3F", 19:"4A", 20:"4B", 21:"4C", 22:"4D", 23:"4E", 24:"4F", 25:"5A", 26:"5B", 27:"5C", 28:"5D", 29:"5E", 30:"5F"}

output = defaultdict(list)

accession = sys.argv[1]
with urlopen("https://public-api.vmit.cucloud.net/vetview_api_19/accession_covid_item_count/%s" % (accession)) as response:
	response_content = response.read()
json_response = json.loads(response_content)

num_samples = json_response['items']
full_sets = math.floor(num_samples / 40)
extra_pools = math.floor((num_samples - full_sets*40) / 5)
remainder = num_samples % 5

for sample in range(num_samples):

	load = math.floor(sample / 96)
	TS = math.floor(sample / 16)
	position = sample % 16
	
	if remainder != 1:
		if sample < full_sets*40:
			row = chr(sample % 8 + 65)
			column = math.floor(sample / 40)
		elif sample < num_samples - remainder:
				row = chr(sample % extra_pools + 65)
				column = full_sets
		else:
				row = chr(extra_pools % 8 + 65)
				column = full_sets
	else:
		if sample < full_sets*40 - 1:
			row = chr(sample % 8 + 65)
			column = math.floor(sample / 40)
		elif sample < num_samples - remainder - 1:
				row = chr(sample % extra_pools + 65)
				column = full_sets
		else:
				row = chr(extra_pools % 8 + 65)
				column = full_sets
	
	output[load].append((sample, TS, position, row, column))	

with open("C:\cu-beckman\csv_files\pooling\pooling_load1.csv", 'w') as out:
	out.write("Source,Source_Well,Destination,Destination_Well\n")
	if len(output[0]) > 0:
		out.write('\n'.join(['%s,%d,Pool,%s%d' % (storage_key[i[1]+1], i[2]+1, i[3], i[4]+1) for i in output[0]]))
	if len(output[1]) > 0:
		out.write('\n')
		out.write('\n'.join(['%s,%d,Pool,%s%d' % (storage_key[i[1]+1], i[2]+1, i[3], i[4]+1) for i in output[1]]))

with open("C:\cu-beckman\csv_files\pooling\pooling_load2.csv", 'w') as out:
	out.write("Source,Source_Well,Destination,Destination_Well\n")
	if len(output[2]) > 0:
		out.write('\n'.join(['%s,%d,Pool,%s%d' % (storage_key[i[1]+1], i[2]+1, i[3], i[4]+1) for i in output[2]]))
	if len(output[3]) > 0:
		out.write('\n')
		out.write('\n'.join(['%s,%d,Pool,%s%d' % (storage_key[i[1]+1], i[2]+1, i[3], i[4]+1) for i in output[3]]))

with open("C:\cu-beckman\csv_files\pooling\pooling_load3.csv", 'w') as out:
	out.write("Source,Source_Well,Destination,Destination_Well\n")
	if len(output[4]) > 0:
		out.write('\n'.join(['%s,%d,Pool,%s%d' % (storage_key[i[1]+1], i[2]+1, i[3], i[4]+1) for i in output[4]]))
	if len(output[5]) > 0:
		out.write('\n')
		out.write('\n'.join(['%s,%d,Pool,%s%d' % (storage_key[i[1]+1], i[2]+1, i[3], i[4]+1) for i in output[5]]))


with open('S:\\biomek\Archive\loadfile_archive\%s_pooling_load1.csv' % (accession), 'w') as out:
	out.write("Source,Source_Well,Destination,Destination_Well\n")
	if len(output[0]) > 0:
		out.write('\n'.join(['%s,%d,Pool,%s%d' % (storage_key[i[1]+1], i[2]+1, i[3], i[4]+1) for i in output[0]]))
	if len(output[1]) > 0:
		out.write('\n')
		out.write('\n'.join(['%s,%d,Pool,%s%d' % (storage_key[i[1]+1], i[2]+1, i[3], i[4]+1) for i in output[1]]))

with open('S:\\biomek\Archive\loadfile_archive\%s_pooling_load2.csv' % (accession), 'w') as out:
	out.write("Source,Source_Well,Destination,Destination_Well\n")
	if len(output[2]) > 0:
		out.write('\n'.join(['%s,%d,Pool,%s%d' % (storage_key[i[1]+1], i[2]+1, i[3], i[4]+1) for i in output[2]]))
	if len(output[3]) > 0:
		out.write('\n')
		out.write('\n'.join(['%s,%d,Pool,%s%d' % (storage_key[i[1]+1], i[2]+1, i[3], i[4]+1) for i in output[3]]))

with open('S:\\biomek\Archive\loadfile_archive\%s_pooling_load3.csv' % (accession), 'w') as out:
	out.write("Source,Source_Well,Destination,Destination_Well\n")
	if len(output[4]) > 0:
		out.write('\n'.join(['%s,%d,Pool,%s%d' % (storage_key[i[1]+1], i[2]+1, i[3], i[4]+1) for i in output[4]]))
	if len(output[5]) > 0:
		out.write('\n')
		out.write('\n'.join(['%s,%d,Pool,%s%d' % (storage_key[i[1]+1], i[2]+1, i[3], i[4]+1) for i in output[5]]))

print(num_samples, end='')