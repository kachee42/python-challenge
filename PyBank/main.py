# This script analyzes bank data from budget_data.csv and determines how many months are being analyzed,
# how much total profit was made over the time period, the average change from one month to the next over the period,
# and the greatest increase and decrease in profits from one month to the next.

# Import operating system module

# Import csv Module

# create an object that contains the path to budget_data.csv

# Open the csv file for analysis

    # Specify the "," as delimiter and create variable to hold the csv contents

    # Skip the header row

    # Place the contents of the csv file into a list for easier analysis

    # Find the length of the list and place into a num_months variable for later use

    # Create a total_profit variable to hold all of the data and set to 0

    # Iterate through each row to find total profit or loss

        # Add the profit value for the month to total_profit

    # Create variable to hold the maximum increase and set it to arbitrarily low number

    # Create variable to hold the date of the maximum increase

    # Create variable to hold the max decrease and set it to an arbitrarily high number

    # create variable to hold the date of the maximum decrease

    # create variable to hold the sum of the changes from one month to the next

    # Iterate through the list one fewer time than num_months

        # create a variable to calculate the change in profit from the next row in the iteration to the current row

        # Create a conditional to check to see if the current change in profit is greater than the maximum increase

            # If yes, set max increase variable equal to the current change in profit

            # If yes, set the variable for the max increase date equal to the next row's date

        # Create a conditional to check to see if the current change in profit is less than the maximum decrease

            # If yes, set max decrease variable equal to current change in profit

            # If yes, set the variable for the max decrease date equal to the next row's date

    # Calculate the average change by dividing the sum of the changes by num_months - 1

    # Print data to command line

    # Publish data to text file
