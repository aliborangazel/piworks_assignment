import csv
import numpy as np

filename_toRead = 'country_vaccination_stats.csv'
filename_toWrite = 'imputed.csv'

with open(filename_toRead, 'r') as csv_to_read:
    csv_reader = csv.reader(csv_to_read)
    header = next(csv_reader) #skip the header
    lines = []
    for row in csv_reader:
        lines.append(row)
    data_count = len(lines)
    lines = np.array(lines)

    with open(filename_toWrite, 'w', newline="") as csv_to_write:
        csv_writer = csv.writer(csv_to_write)
        csv_writer.writerow(header)

        # exploit the format in the data (alphabetically ordered, hence, consecutive lines for the same country)
        country = "smt"
        high_test_number = 1e9
        vaccinations = np.ones(data_count) * high_test_number
        countryStartingIndex = counter = 0
        for line in lines:

            if (country != line[0]): # new country
                country = line[0]
                if counter != 0: # if not at the beginning, replace previous countries' empty values with mins
                    m = min(vaccinations[countryStartingIndex:counter])
                    min_indices = np.where(vaccinations[countryStartingIndex:counter] == high_test_number)[0] # indices at which we have empty values
                    if (m != high_test_number):
                        lines[countryStartingIndex + min_indices, 2] = str(int(m)) # fill with the min
                    else:
                        lines[countryStartingIndex + min_indices, 2] = '0' # fill with 0 (no data)
                    countryStartingIndex = counter

            if line[2]: # if vaccination is not empty
                vaccinations[counter] = int(line[2])
            counter += 1

        # replace the last countries' empty values with its min
        m = min(vaccinations[countryStartingIndex:counter])
        min_indices = np.where(vaccinations[countryStartingIndex:counter] == high_test_number)[0] # indices at which we have empty values
        if (m != high_test_number):
            lines[countryStartingIndex + min_indices, 2] = str(int(m)) # fill with the min
        else:
            lines[countryStartingIndex + min_indices, 2] = '0' # fill with 0 (no data)
        csv_writer.writerows(lines)

    

