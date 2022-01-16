#!/usr/bin/env python3

import csv
import json
from pprint import pprint

# load the input.csv file
with open('input.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# make an empty list
json_output = []
for row in rows:

    # define how to translate the CSV to correct type of JSON
    item =  {
        'title': row['title'],
        'subtitle': row['subtitle'],
        'ranges': [
            float(row['range_min']),
            float(row['range_mid']),
            float(row['range_max'])],
        'measures': [
            float(row['measure_min']),
            float(row['measure_max'])],
        'markers': [float(row['markers'])]
    }
    # add to the empty list
    json_output.append(item)

# output to json
with open('output.json', 'w') as f:
    json.dump(json_output, f, indent=4)


# test out the json output
# pprint(json_output)
