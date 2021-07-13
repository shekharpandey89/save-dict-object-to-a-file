# dict_to_csv_2.py

import csv

csvColumns = ['City', 'Country', 'Rank']
dictDemo = [
    {'City': 'New York', 'Country': 'USA', 'Rank': 3},
    {'City': 'Sydney', 'Country': 'Australia', 'Rank': 5},
    {'City': 'Dubai', 'Country': 'UAE', 'Rank': 10},
    {'City': 'Mumbai', 'Country': 'India', 'Rank': 17},
    {'City': 'Bejing', 'Country': 'China', 'Rank': 7},
]
csvFileName = "data.csv"
try:
    with open(csvFileName, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=csvColumns)
        writer.writeheader()
        for data in dictDemo:
            writer.writerow(data)
except IOError:
    print("Got Error")