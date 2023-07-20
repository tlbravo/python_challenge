 # Import modules
import os
import csv

#Specify the path to open/collect the data from the Resources folder.
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#Statement to open the csv file. 
with open(budget_data_csv, encoding='UTF-8') as budget:
   
    # Specify the delimiter and the variable that holds data.
    csvreader = csv.reader(budget, delimiter=",")
   
    #Skip the header row.
    csvheader = next(csvreader) 

    #Create empty lists for the data being iterated is collected. 
    date_info = []
    profit_lossess_info = []
    
    #Specify each column of csv file and make sure that the data collected gets added to a new variable.
    for row in csvreader:
        dates = row[0]
        date_info.append(dates)
        profit_lossess = int(row[1])   
        profit_lossess_info.append(profit_lossess)

    #Total months. Length of column A.
    total_months = len(date_info)

    #Total profit/losses. Total of column B.
    for row in profit_lossess_info: 
        net_total_profit_losses = sum(profit_lossess_info)
    
    #Average Change of profits/losses. Calculate changes each months. 
    changes = 0
    total_change = 0
    for x in range (1, len(profit_lossess_info)):
        changes = [profit_lossess_info[x] - profit_lossess_info[x-1]]
        #Any changes are added to the previously empty variable.
        total_change += sum(changes)
        #There are 85 changes in the data.
        average_change = total_change / total_months
    
    #Greatest increase in profits.
        greatest_increase = max(profit_lossess_info)
    #Find the month of the greatest increase in profits.
        greatest_increase_month = date_info[profit_lossess_info.index(greatest_increase) + 1]

    #Greatest decrease in profits.
        greatest_decrease = min(profit_lossess_info)
    #Find the month of the greatest decrease in profits.
        greatest_decrease_month = date_info[profit_lossess_info.index(greatest_decrease) + 1]
    
#Print results   
print(f"Total Months: {total_months}")
print(f"Total: + ${net_total_profit_losses}")
print(f"Average Change: + ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}")

#Output results into a text file
results_file = os.path.join("analysis", "budget_data.txt")
with open(results_file, "w") as results:

    results.write("Financial Analysis\n")
    results.write("-------------------------------\n")
    results.write(f"Total Months: {total_months}\n")
    results.write(f"Total: ${net_total_profit_losses}\n")
    results.write(f"Average Change: {average_change} \n")
    results.write(f"Greatest Increase in Profits: {greatest_increase_month} {greatest_increase}\n")
    results.write(f"Greatest Decrease in Profits: {greatest_decrease_month} {greatest_decrease}\n")