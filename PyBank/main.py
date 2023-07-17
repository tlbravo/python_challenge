 # Import modules
import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('python_challenge', 'PyBank', 'Resources', 'budget_data.csv')

# Set text file for results
text_path = "output.txt"

# Definte variables and lists to store values
total_months = 0
total_months = []
total_revenue = 0
total_revenue = []
greatest_increase_profits = 0
greatest_decrease_profits = 0

with open(budget_data_csv, encoding='UTF-8') as budget:
    # Specify the delimiter and the variable that holds contents
    csvreader = csv.reader(budget, delimiter=",")
    # Make sure the code skips the header row 
    csvheader = next(csvreader) 
    # Date = column A and Profits/Loss = column B
    for row in csvreader:
        total_months.append(row[0])
        total_revenue.append(row[1])
    

    #Total Profits
    total_profits = [int(x) for x in total_revenue]
    total_profits_max= sum(total_profits) 
   
    #Average Change
    profit_losses = 0
    average_changes = []
    for x in range (1, len(profit_losses)):
        average_changes - profit_losses[x] - profit_losses[x-1]
        average_changes.append(average_changes)
        average_changes = sum(average_changes) / len(average_changes)
    #Greatest increase in profits 
    greatest_increase_profits = max(average_changes)

    #Greatest decrease in profits
    greatest_decrease_profits = min(average_changes)

    print("Total Months: ", len(total_months))
    print ("Net Total Profits/Losses: ", total_profits_max)
    print ("Average Change: ", average_changes)
    print ("Greatest Increase in Profits: ", greatest_increase_profits)
    print ("Greatest Decrease in Profits: ", greatest_decrease_profits)