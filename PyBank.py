import os
import csv
import statistics

print('                        ')
print('Financial Analysis')
print('________________________')
print('                        ')

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvfile)

	num_rows = 0
	sum_money = 0
	average = 0
	count = 0 
	previous_value = 0
	change = []
	diff = 0
	months = []
	
	for row in csvreader:
		if(count == 0):
			previous_value = row[1]
		else:
			diff = int(row[1]) - int(previous_value)
			change.append(diff)
			previous_value = int(row[1])
		count = count + 1		
		sum_money += int(row[1])
		change.append(diff)
		months.append(row[0])
	

	print('Total Months: ' + str(count))
	print(f'Total: ${str(sum_money)}')
	print(f'Average Profit/Loss: ${str(statistics.mean(change))}')
	print(f'Greatest Increase in Profits: ' + str(max(months))  + str(max(change)))
	print(f'Greatest Decrease in Profits: ' + str(min(months)) +  str(min(change)))
