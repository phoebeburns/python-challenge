#loop through rows of budget_data to calculate:
#   -total number of months included in the dataset
#   -The net total amount of "Profit/Losses" over the entire period
#   -Calculate the changes in "Profit/Losses" over the entire period, 
#       then find the average of those changes
#   -The greatest increase in profits (date and amount) over the entire period
#   -The greatest decrease in profits (date and amount) over the entire period
#   looking forward to doing this type of thing with pandas


# Modules
import os
import csv

#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
#txtpath = os.path.join('..', 'Analysis/')

csvpath = 'c:/users/lunaclara/python-challenge/pybank/resources/budget_data.csv'
txtpath = 'c:/users/lunaclara/python-challenge/pybank/Analysis/'

#Set numerical variables to 0
months = 0
total = 0
minVal = 0
maxVal = 0

#Open CSV reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    #Loop through rows, performing calculations
    for row in csvreader:
        months = months + 1

        total = total + int(row[1])
        avgMonth = total/months
        
        if int(row[1]) > maxVal:
            maxVal = int(row[1])
            maxDate = row[0]
        elif int(row[1]) < minVal:
            minVal = int(row[1])
            minDate = row[0]

#List of items to print/export
lines = ["Financial Analysis","------------------","Total Months: " + str(months), 
"Average Change: "+ '${:,.2f}'.format(avgMonth),
"Greatest Increase In Profits: " + maxDate + " " + '${:,.2f}'.format(maxVal),
"Greatest Decrease In Profits: " + minDate + " " + '${:,.2f}'.format(minVal) ]

#Print to screen
for line in lines:
    print(line)

#Print to text file
with open(txtpath + 'FinancialAnalysis.txt','w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')