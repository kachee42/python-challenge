# This script looks through the voting data for multiple counties and tallies the number of votes for each candidate
# Tallies are then used to determine win percentages and a final winner
# These data are printed to the command line and exported to a text file

# Import operating system Module
import os

# Import CSV module
import csv

# Create variable that contains the file path of the CSV
election_csv = os.path.join('resources', 'election_data.csv')

# Open the CSV for analysis
with open(election_csv) as csvfile:

    # run CSV reader, specify the delimiter and place the data into a variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip Header
    header = next(csvreader)

    # Place data into list for easier analysis
    election_data = list(csvreader)

    # Count total number of votes
    num_total_votes = len(election_data)

    # Create an empty dictionary to hold the number of candidates and vote tallies
    candidates = {}

    # Iterate through each vote in the election data
    for votes in election_data:

        # set candidate name equal to the value in column 3
        candidate_name = votes[2]

        # Conditional to check if the candidate name on the current line is not in the dictionary
        if candidate_name not in candidates.keys():

            # If candidate is not in the dictionary add them and set the vote tally to 0, this vote will tick up each time this candidate appears
            candidates[candidate_name] = 0

        # Add one to the vote tally in the dictionary definition for the candidate
        candidates[candidate_name] += 1

    # Create a winning votes variable and set it to 0, this will change to the largest number of votes later
    winning_votes = 0

    # Create a winner variable and set it to ' ', this will be changed to the candidate with the most votes later
    winner = ' '

    # Print Election results and underline lines
    print('Election Results')
    print('--------------------------')

    # print the total votes and next underline lines
    print('Total Votes: %d' % num_total_votes)
    print('--------------------------')

    # Iterate through each candidate in the dictionary

        # Conditional to check if the votes for each candidate is greater than the winning votes variable

            # if yes, set the winning votes equal to the candidate's definition number of votes

            # if yes, set the winner variable equal to the candidate

        # Print each candidate name, the percentage of votes won (calculated here), and the dictionary definition number of votes for that candidate

        # Print underline, winner name and last underline

    # Create output path and analysis file name

    # Open and create textfile

        # write Title line and underline

        # write total votes line and underline

        # Iterate through each candidate in dictionary

            # Conditional to check if currently looked at candidate's votes are greater than the winning votes variable

                # If yes, change the winning votes variable to candidate votes

                # if yes, change the winner variable to the current candidate

            # for each candidate write the candidate name, calculated percent votes wone, and the number of votes won

        # write underline, winner name, and final underline