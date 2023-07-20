 # Import modules
import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")

total_vote_count = 0
vote_percent = []
candidate_list = []
votes = 0
candidate_votes = {}
Stockham_votes = 0
DeGette_votes = 0
Doane_votes = 0



with open(election_data_csv, encoding='UTF-8') as election:
    
    # Specify the delimiter and the variable that holds contents
    csvreader = csv.reader(election, delimiter=",")
    
    # Make sure the code skips the header row 
    csvheader = next(csvreader) 
    
    for row in csvreader:
    #Total number of votes cast
        total_vote_count += 1   
        candidate = row[2]
        if candidate in candidate_list:
            candidate_votes[candidate] +=1
        else:
            candidate_votes[candidate] = 1 
            candidate_list.append(candidate)

#Calculate Percentage of votes for each candidate


#Calaculate winner
#winner = total_vote_count.index(max(str(total_vote_count)))                                              


#Print Results
print("Election Results")
print("-------------------------------")
print("Total Votes: " + total_vote_count)

#print("Charles Caster Stockham:" + str(candidate["Charles Caster Stockham Votes"] + "%" + str(candidate["Charles Caster Stockham"])))
#print("Diana DeGette:" + str(candidate["Diana DeGette"] + "%" + str(candidate["Diana DeGette"])))
#print("Raymon Anthony Doane:" + str(candidate["Raymon Anthony Doane"] + "%" + str(candidate["Raymon Anthony Doane"])))
#print("Winner :" (candidate[winner]))