#Import Packages
import os
import csv

#Establish file path and open file
poll_path = os.path.join("Resources","election_data.csv")
with open(poll_path, 'r') as csvfile:
    poll_csv = csv.reader(csvfile, delimiter=',')
    #Read header first to remove from row loop
    csv_header = next(poll_csv)
    print(csv_header)

