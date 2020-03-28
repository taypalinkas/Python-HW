import os
import csv
import statistics
import string


csvpath = os.path.join('..', 'Resources', 'election_data_1.csv')

with open(csvpath, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvfile)

	count = 0
	

	for row in csvreader:
	
		count = count + 1

		name = row[2]

		Khan = name.count("Khan")

		print(str(Khan))
	
	print('                      ')
	print('Election Results')
	print('                      ')
	print('______________________')
	print('                      ')
	print(f'Total Votes: {(str(count))}')
	print('                      ')
	print('______________________')
	print('                      ')