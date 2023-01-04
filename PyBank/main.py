# This script analyzes bank data from budget_data.csv and determines how many months are being analyzed,
# how much total profit was made over the time period, the average change from one month to the next over the period,
# and the greatest increase and decrease in profits from one month to the next.

# Import operating system module
import os

# Import csv Module
import csv

# create an object that contains the path to budget_data.csv
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Open the csv file for analysis
with open(budget_csv) as csvfile:

    # Specify the "," as delimiter and create variable to hold the csv contents
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip the header row
    header = next(csvreader)

    # Place the contents of the csv file into a list for easier analysis
    profit_data = list(csvreader)

    # Find the length of the list and place into a num_months variable for later use
    num_months = len(profit_data)

    # Create a total_profit variable to hold all of the data and set to 0
    total_profit = 0

    # Iterate through each row to find total profit or loss
    for row in profit_data:

        # Add the profit value for the month to total_profit
        total_profit += int(row[1])

    # Create variable to hold the maximum increase and set it to arbitrarily low number
    max_increase = -99999999

    # Create variable to hold the date of the maximum increase
    max_increase_date = None

    # Create variable to hold the max decrease and set it to an arbitrarily high number
    max_decrease = 99999999

    # create variable to hold the date of the maximum decrease
    max_decrease_date = None

    # create variable to hold the sum of the changes from one month to the next
    total_change = 0

    # Iterate through the list one fewer time than num_months
    for row_index in range(num_months - 1):

        # create a variable to calculate the change in profit from the next row in the iteration to the current row
        profit_change = int(profit_data[row_index + 1][1]) - int(profit_data[row_index][1])

        # Create a conditional to check to see if the current change in profit is greater than the maximum increase
        if profit_change > max_increase:

            # If yes, set max increase variable equal to the current change in profit
            max_increase = profit_change

            # If yes, set the variable for the max increase date equal to the next row's date
            max_increase_date = profit_data[row_index+1][0]

        # Create a conditional to check to see if the current change in profit is less than the maximum decrease
        if profit_change < max_decrease:

            # If yes, set max decrease variable equal to current change in profit
            max_decrease = profit_change

            # If yes, set the variable for the max decrease date equal to the next row's date
            max_decrease_date = profit_data[row_index+1][0]

        # Calculate the sum of the total changes in profits
        total_change += profit_change

    # Calculate the average change by dividing the sum of the changes by num_months - 1
    avg_change = float(total_change / (num_months-1))

    # Print data to command line
    print('Financial Analysis')
    print('---------------------------')
    print('Total Months: %d' % num_months)
    print('Total: $%d' % total_profit)
    print('Average Change: $%.2f' % avg_change)
    print('Greatest Increase in Profits: %s ($%d)' % (max_increase_date, max_increase))
    print('Greatest Decrease in Profits: %s ($%d)' % (max_decrease_date, max_decrease))

# Create path and name for text file
output_path = os.path.join("analysis", "Analysis.txt")

# Open new text file
with open(output_path, 'w') as textfile:

    # Publish data to text file
    textfile.write('Financial Analysis\n\n')
    textfile.write('---------------------------\n\n')
    textfile.write('Total Months: %d\n\n' % num_months)
    textfile.write('Total: $%d\n\n' % total_profit)
    textfile.write('Average Change: $%.2f\n\n' % avg_change)
    textfile.write('Greatest Increase in Profits: %s ($%d)\n\n' % (max_increase_date, max_increase))
    textfile.write('Greatest Decrease in Profits: %s ($%d)\n\n' % (max_decrease_date, max_decrease))