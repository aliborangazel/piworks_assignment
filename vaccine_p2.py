import csv
import numpy as np

filename_toRead = 'imputed.csv'

with open(filename_toRead, 'r') as csv_to_read:
    csv_reader = csv.reader(csv_to_read)
    next(csv_reader)    #skip the header
    lines = []
    for row in csv_reader:
        lines.append(row)
    data_count = len(lines)
    lines = np.array(lines)

    # read country by country. Once a country is complete, find its median. Compare with the previous min median.
    country = "smt"

    highest_medians = {
        "c1" : 0,
        "c2" : 1,
        "c3" : 2
    }

    vaccinations = np.zeros(data_count)
    countryStartingIndex = counter = 0
    for line in lines:
        vaccinations[counter] = int(line[2])

        if (country != line[0]):    # new country
                                    # previous countries' operations (finding median and updating dict)
            if counter != 0:        # if not at the beginning (there must be a "previous" country), find median
                med = np.median(vaccinations[countryStartingIndex:counter])
                countryStartingIndex = counter
                min_median_key = min(highest_medians, key = highest_medians.get)
                if (med > highest_medians[min_median_key]): # if the new median is smaller than max of the dict 
                    highest_medians[country] = med          # add the new minimum
                    highest_medians.pop(min_median_key)     # remove the maximum among the three medians
            country = line[0]

        counter += 1

                                                # calculate the median for the last country
    med = np.median(vaccinations[countryStartingIndex:counter])
    countryStartingIndex = counter
    min_median_key = min(highest_medians, key = highest_medians.get)
    if (med > highest_medians[min_median_key]): # if the new median is bigger than min of the dict 
        highest_medians[country] = med          # add the new max
        highest_medians.pop(min_median_key)     # remove the min among the three medians
    
    highest_medians = {key:value for key,value in sorted(highest_medians.items(), key= lambda item:item[1], reverse=True)}
    print("\nTop 3 Countries with Highest Medians:")
    for key in highest_medians.keys():
        print(key + " : " + str(highest_medians[key]))
    

