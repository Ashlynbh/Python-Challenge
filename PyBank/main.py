#######
#PREPARE
#######

#IMPORT LIBRARIES 
from calendar import month
import os 
import csv
from statistics import mean
import statistics

# DEFINING VARIABLES
total_months = 0 
total = 0
previous = 0
profit_change = []
monthly_change = []
months_list = []

#######
#ACCESS DATA 
#######

#LOCATE THE DATA 
budget_csv = os.path.join("Resources", "Budget.csv")

# OPEN AND READ DATA 
with open(budget_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header = next (csv_file) 
    

    for row in csvreader:

#SPLIT DATA INTO TWO LISTS  
# MONTHS  
        months = row
        months_list.append(months[0])

#CHANGES IN PROFIT AND LOSS
        profit_change = (int(row[1]) - previous)
        monthly_change.append(profit_change)
        previous = int(row[1])  

# #Calculate Total Months 
        total_months += 1

#Calculate Total Profit/Loss 
        total += int(row[1])

# #######
# #ANALYSE DATA
# #######

#Because the first value in the list is not a change
#We need to delete it 
    del monthly_change[0]
    print(f"test {monthly_change}")


#Calculate average 
    avg = mean(monthly_change)

#The greatest increase in profit (amount) over the entire period
    max_inc = max(monthly_change)

#The greatest increase in revenue (date) over the entire period 
    max_numbers = max(monthly_change)
    max_index = monthly_change.index(max(monthly_change))
    max_exact_index = max_index +1
    increase_month = months_list[max_exact_index]

#The greatest decrease in profit (amount) over the entire period
    max_dec = min(monthly_change)

#The greatest increase in revenue (date) over the entire period 
    min_number = min(monthly_change)
    min_index = monthly_change.index(min(monthly_change))
    min_exact_index = min_index +1
    decrease_month = months_list[min_exact_index]

#######
#PRINT ANALYSIS
#######

output = (
        f"Financial Analysis\n"
        f"----------------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total Profit/Loss: ${total}\n"
        f"Average Change: ${round(avg,2)}\n"
        f"Greatest Increase in Profits: {increase_month}(${str(max_inc)})\n"
        f"Greatest Decrease in Profits: {decrease_month}(${str(max_dec)})\n"

)
#print output to terminal 
print(output)

text_file = open("Financial.txt", "w")
n = text_file.write(output)
text_file.close()

