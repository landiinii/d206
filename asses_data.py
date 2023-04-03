import csv

csvfile = open('churn_raw_data.csv', 'r', newline='')
datareader = csv.reader(csvfile)
next(datareader)
for row in datareader:
    print(', '.join(row))
    break

csvfile.close()
