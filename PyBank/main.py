#import os module
import os

#import csv module 
import csv

#set up and define variables
counter=0
total=0
average_change=0
greatest_profit = 0
greatest_loss = 0
change = []
months = []
prevrowprofit = 0

#set the path for csv file 
filepath = "Resources/budget_data.csv"

# Read the csv and convert it into a list of dictionaries
with open(filepath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter= ",")
    # skip the header
    header = next(csv_reader)
    #printing the headers to make sure it's pulling from the document correctly
    #print(header)
   
    #loop through the csv file
    for row in csv_reader:
        #let's run some calculations!
        if counter == 0:
            prevrowprofit = int(row[1])
        #calculate the total number of months 
        counter += 1
        #calculate total profit/losses
        total += int(row[1])
        #calculate changes per month
        current_change = int(row[1])-prevrowprofit
        change.append(current_change)
        months.append(row[0])
        #on to the next row
        prevrowprofit = int(row[1])
        #find the greatest increase
        if current_change > greatest_profit:
                  greatest_profit = current_change
                  greatest_profit_month = str(row[0])
        #find the greatest decrease
        if current_change < greatest_loss:
                  greatest_loss = current_change
                  greatest_loss_month = str(row[0])

#find the average monthly change                
change.pop(0)
months.pop(0)
average_change = sum(change)/len(change)

#find the dates for the greatest increases and decreases
max_index = change.index(max(change))
max_months = months[max_index]
min_index = change.index(min(change))
min_months = months[min_index]

#Format the data
Formated_Total = "{:,.2f}".format(total)
Formated_Average_Change = "{:,.2f}".format(average_change)
Formated_Greatest_Profit = "{:,.2f}".format(greatest_profit)
Formated_Greatest_Loss = "{:,.2f}".format(greatest_loss)

#Have the data presented in the appropriate formatting for the consumer
print("Financial Analysis")
print("--------------------")
print(f"Total Months:{counter}")
print(f"Total: ${Formated_Total}")
print(f"Average Change: ${Formated_Average_Change}")
print(f"Greatest Increase in Profits: {max_months} (${Formated_Greatest_Profit})")
print(f"Greatest Decrease in Profits: {min_months} (${Formated_Greatest_Loss})")

#create a text file for the above financial analysis
filename = "Financial Analysis.txt"
outfile = open(filename, 'w')
outfile.write("Financial Analysis")
outfile.write("\n----------------------------------------")
outfile.write(f"\nTotal Months: {counter}")
outfile.write(f"\nTotal: ${Formated_Total}")
outfile.write(f"\nAverage Change: ${Formated_Average_Change}")
outfile.write(f"\nGreatest Increase in Profits: {max_months} (${Formated_Greatest_Profit})")
outfile.write(f"\nGreatest Decrease in Profits: {min_months} (${Formated_Greatest_Loss})")

outfile.close()
