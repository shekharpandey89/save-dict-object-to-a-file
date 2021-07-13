#dict_to_file_asJSON.py

import json

dictDemo = [
    {'City': 'New York', 'Country': 'USA', 'Rank': 3},
    {'City': 'Sydney', 'Country': 'Australia', 'Rank': 5},
    {'City': 'Dubai', 'Country': 'UAE', 'Rank': 10},
    {'City': 'Mumbai', 'Country': 'India', 'Rank': 17},
    {'City': 'Bejing', 'Country': 'China', 'Rank': 7},
]

filename = "dict.json"

# Writing the list of dict objects to a file
with open(filename, mode='w') as f:
    json.dump(dictDemo, f)

# Writing a new dict object to a file as append and overwrite the whole file
with open(filename, mode='w') as f:
    dictDemo.append({'City': 'Bejing', 'Country': 'China'})
    json.dump(dictDemo, f)