# Modules
import os
import csv

previous_pl_value = 0 
# number of months included in dataset
month_count = 0
# net total amount of Profit/Losses
net_total_amount = 0
# average changes in Profit/Losses
sum_of_changes = 0
total_change = 0
average_changes = 0 
counter = 1
# greatest increase in profits (date and amount) over the entire period
# greatest decrease in losses (date and amount) over the entire period
comparisons = {
    "greatest_increase": "0",
    "greatest_increase_date": "",
    "greatest_decrease": "0",
    "greatest_decrease_date": ""
}


# Set path for file for read file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header and sum month in dataset
    for row in csvreader:
        if (row[1] is not "") and (row[1] is not ""): # do not process last line
            month_count += 1
            net_total_amount += int(row[1])
            total_change = int(row[1]) - previous_pl_value
   
            if counter >= 2:
                sum_of_changes += total_change

            if total_change > int(comparisons["greatest_increase"]):
                comparisons["greatest_increase"] = total_change
                comparisons["greatest_increase_date"] = row[0]
            elif total_change < int(comparisons["greatest_decrease"]):
                comparisons["greatest_decrease"] = total_change
                comparisons["greatest_decrease_date"] = row[0]
                    
            
            previous_pl_value = int(row[1])
            counter += 1

    average_changes = sum_of_changes/(month_count -2)


    print(f"total months: {month_count}")
    print(f"net total: ${net_total_amount}")
    print(f"average: {average_changes}")
    print(f'greatest increase in profits: {comparisons["greatest_increase_date"]} {comparisons["greatest_increase"]}')
    print(f'greatest decrease in profits: {comparisons["greatest_decrease_date"]} {comparisons["greatest_decrease"]}')




# Specify the file to write to
#output_path = os.path.join("..", "output", "budget_data_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
txtfile = open("Resources/budget_data_results.txt", "w+")
txtfile.write(f"total months: {month_count}\n")
txtfile.write(f"net total: ${net_total_amount}\n")
txtfile.write(f"average: {average_changes}\n")
txtfile.write(f'greatest increase in profits: {comparisons["greatest_increase_date"]} {comparisons["greatest_increase"]}\n')
txtfile.write(f'greatest decrease in profits: {comparisons["greatest_decrease_date"]} {comparisons["greatest_decrease"]}')
