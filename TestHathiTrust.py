import glob
import pandas as pd
from htrc_features import FeatureReader
import csv
with open('C:\\hathi\\Students.csv', 'r') as f:
    reader = csv.reader(f)
    hathi_list = list(reader)

for i in hathi_list:
    try:
        print('Grabbing tokenlist for: ', i)
        fr = FeatureReader(ids=i)
        for vol in fr:
            tokens = vol.tokenlist()
            tokens.to_dict()
            #matches = tokens['count'] > 10
            #tokens[matches].sample(100)
            filename = 'C:\\hathi\\' + str(i) + '.txt'
            file = open(filename, 'w')
            file.write(str(tokens))
    except:
        pass




