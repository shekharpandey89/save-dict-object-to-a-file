# dict_to_csv.py
import csv

dict_sample = {'name': 'LinuxHint', 'city': 'CA', 'education': 'Engineering'}

with open('data.csv', 'w') as f:
    for key in dict_sample.keys():
        f.write("%s, %s\n" %(key, dict_sample[key]))