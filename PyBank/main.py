import os
import csv

budgetpath = os.path.join("PyBank/Resources/budget_data.csv")

total_months = 0
with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile)
    if csv.Sniffer().has_header: #skip the header #I've run into comma vs pipe delimited 
        #issues at my job, my manager knows python he told me to always use the sniffer. 
        # I hope that's ok
        next(budgetreader)
    for row in budgetreader:
        total_months += 1



total_profits = 0
with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile)
    if csv.Sniffer().has_header: #skip the header
        next(budgetreader)
    for row in budgetreader:
        total_profits += int(row[1])

    
profit_list =[]

with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile)
    next(budgetreader)
    for row in budgetreader:
        profit_list.append(row[1])

month_values = list(map(int, profit_list))

monthly_change = [month_values[i + 1] - month_values[i] for i in range(len(month_values)-1)]

total_change = sum(monthly_change)

avg_change_profit = total_change / len(month_values)


max_value = max(month_values)
min_value = min(month_values)

def find_row(input):
    csvfile = open(budgetpath)
    budgetreader = csv.reader(csvfile)
    for row in budgetreader:
        if row[1] == input:
            return budgetreader.line_num


max_value_index = find_row(str(max_value))
min_value_index = find_row(str(min_value))

all_rows = []

with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile)
    for row in budgetreader:
        all_rows.append(row)


max_string = all_rows[max_value_index-1]
min_string = all_rows[min_value_index-1]

# print to terminal
print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profits}')
print(f'Average Change: ${avg_change_profit}')
print(f'Greatest Increase in Profits: {max_string}')
print(f'Greatest Decrease in Profits: {min_string}')

# print to text file
write_path = open('PyBank Output.txt', 'w')
write_path.write(f'Financial Analysis\n')
write_path.write(f'-------------------------\n')
write_path.write(f'Total Months: {total_months}\n')
write_path.write(f'Total: ${total_profits}\n')
write_path.write(f'Average Change: ${avg_change_profit}\n')
write_path.write(f'Greatest Increase in Profits: {max_string}\n')
write_path.write(f'Greatest Decrease in Profits: {min_string}\n')



