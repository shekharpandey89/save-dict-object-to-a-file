#dict_to_txt_2.py

""":cvar
    This code will save the dict objects in the file with the
    append mode.
"""
dictDemo = [
    {'City': 'New York', 'Country': 'USA', 'Rank': 3},
    {'City': 'Sydney', 'Country': 'Australia', 'Rank': 5},
    {'City': 'Dubai', 'Country': 'UAE', 'Rank': 10},
    {'City': 'Mumbai', 'Country': 'India', 'Rank': 17},
    {'City': 'Bejing', 'Country': 'China', 'Rank': 7},
]

filename = "dict_to_file_appendMode.txt"

# Writing the list of dict objects to a file
with open(filename, mode='a') as f:
    f.write(str(dictDemo))
