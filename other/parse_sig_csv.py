import os
import csv
import ast

sig_csv = "./wiki_file_sigs.csv"

with open(sig_csv, "r") as f:
    csv_reader = csv.DictReader(f)
    
    import pprint
    
    #pprint.pprint(csv_reader)
    
    for row in csv_reader:
        pprint.pprint(dict(row))
        #try:
            #file_exts = row['file_extension']
        #except:
            #file_exts = None
        #print(file_exts)
        #print(row['hex'])
    