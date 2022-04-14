import csv

filename_toRead = 'imputed.csv'

with open(filename_toRead, 'r') as csv_to_read:
    csv_reader = csv.reader(csv_to_read)
    next(csv_reader)    #skip the header

    sum = 0
    for line in csv_reader:
        if line[1] == "1/6/2021":
            sum += int(line[2])
    print(sum)