#dict_to_txt.py

dictDemo = [
    {'City': 'New York', 'Country': 'USA', 'Rank': 3},
    {'City': 'Sydney', 'Country': 'Australia', 'Rank': 5},
    {'City': 'Dubai', 'Country': 'UAE', 'Rank': 10},
    {'City': 'Mumbai', 'Country': 'India', 'Rank': 17},
    {'City': 'Bejing', 'Country': 'China', 'Rank': 7},
]

filename = "dict.txt"

# Writing the list of dict objects to a file
with open(filename, mode='w') as f:
    f.write(str(dictDemo))

