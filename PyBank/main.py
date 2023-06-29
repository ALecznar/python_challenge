import csv
import os

budget_data_csv = "budget_data.csv"




# declare my variables
months = 0
money = 0
profit = 0
changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]


#open csv

with open(budget_data_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    
    #skip first row of data
    header = next(csv_reader)


    #loop through rows
    for row in csv_reader:
        months = months + 1
        money =  money + int(row[1])
        
        current_profit = int(row[1])
        change = current_profit - profit
        changes.append(change)
        profit = current_profit
        
        
        
        
        #greatest increase and decrease
        
        if change > greatest_increase[1]:
            greatest_increase = [row[0], change]
            
        if change < greatest_decrease[1]:
            greatest_decrease = [row[0], change]
        
average_change = sum(changes) / len(changes) 



#print results to screen

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total Money: ${money}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
        


text_file = "financial_analysis.txt"


with open(text_file, "w") as file:
    # type results to text file
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total Money: ${money}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
