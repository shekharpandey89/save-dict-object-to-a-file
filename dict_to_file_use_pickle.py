# dict_to_file_use_pickle.py

import pickle

dictDemo = [
    {'City': 'New York', 'Country': 'USA', 'Rank': 3},
    {'City': 'Sydney', 'Country': 'Australia', 'Rank': 5},
    {'City': 'Dubai', 'Country': 'UAE', 'Rank': 10},
    {'City': 'Mumbai', 'Country': 'India', 'Rank': 17},
    {'City': 'Bejing', 'Country': 'China', 'Rank': 7},
]

filename = "picklefile.pkl"

with open(filename, 'ab') as f:
    pickle.dump(dictDemo,f)
