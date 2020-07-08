#Import Packages
import os
import csv

#Establish file path and open file
bank_path = os.path.join("Resources","budget_data.csv")
with open(bank_path, 'r') as csvfile:
    bank_csv = csv.reader(csvfile, delimiter=',')
    #Read header first to remove from row loop
    csv_header = next(bank_csv)
    #Establish variables
    row_total = 0
    pnl = 0
    delta_pairs = []
    delta_value = 0
    prev_value = "hold"
    cur_value = 0
    #Loop through rows, grab data and make calculations
    for row in bank_csv:
        row_total += 1
        pnl += int(row[1])
        cur_value = int(row[1])
        if prev_value != "hold":
            delta_value = cur_value - prev_value
            delta_pairs.append([row[0],int(delta_value)])
        prev_value = cur_value

#Additional calculations
max_val = 0
max_date = "hold"
min_val = 0
min_date = "hold"
delta_sigma = 0
for a,b in delta_pairs:
    if b > max_val:
        max_date = a
        max_val = b
    if b < min_val:
        min_date = a
        min_val = b
    delta_sigma += b
delta_average = delta_sigma / len(delta_pairs)

print(f'\nFinancial Analysis\n------------------\n'
    f'Total Months: {row_total}\nNet Profit: ${pnl}\n'
    f'Average Change: {delta_average}\n'
    f'Greatest Profit Increase: {max_date} ${max_val}\n'
    f'Greatest Profit Decrease: {min_date} ${min_val}')

output_path = os.path.join("Analysis","output.txt")
with open(output_path, 'w') as txtfile:
    print(f'\nFinancial Analysis\n------------------\n'
    f'Total Months: {row_total}\nNet Profit: ${pnl}\n'
    f'Average Change: {delta_average}\n'
    f'Greatest Profit Increase: {max_date} ${max_val}\n'
    f'Greatest Profit Decrease: {min_date} ${min_val}',file = txtfile)
