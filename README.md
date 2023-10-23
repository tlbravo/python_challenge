# Module 3 Challenge
* I used python scripting to analyze finalcial records for PyBank and to modernize a vote counting process for PyPoll with the data provided in the budget_data and election data CSV files.
* The python codes and text files containing my calculations are included. I followed the example in the following website in order to output txt files with my results: https://www.pythontutorial.net/python-basics/python-write-text-file/.**


# PyBank Instructions

In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
Your task is to create a Python script that analyzes the records to calculate each of the following values:
  1. The total number of months included in the dataset
  2. The net total amount of "Profit/Losses" over the entire period
  3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
  4. The greatest increase in profits (date and amount) over the entire period
  5. The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results: <br>
* Financial Analysis <br>
* Total Months: 86 <br>
* Total: $22564198 <br>
* Average Change: $-8311.11 <br>
* Greatest Increase in Profits: Aug-16 ($1862002) <br>
* Greatest Decrease in Profits: Feb-14 ($-1825558) <br>

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# PyPoll Instructions

In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
  1. The total number of votes cast
  2. A complete list of candidates who received votes
  3. The percentage of votes each candidate won
  4. The total number of votes each candidate won
  5. The winner of the election based on popular vote

Your analysis should align with the following results:

Election Results
*  Total Votes: 369711
* Charles Casper Stockham: 23.049% (85213)
* Diana DeGette: 73.812% (272892)
* Raymon Anthony Doane: 3.139% (11606)
* Winner: Diana DeGette <br>

In addition, your final script should both print the analysis to the terminal and export a text file with the results.