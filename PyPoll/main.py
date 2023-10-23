 # Import modules.
import os
import csv

# Path to collect data from the Resources folder.
election_data_csv = os.path.join("Resources", "election_data.csv")
results = []
total_vote_count = 0
candidate_list = []
candidate_votes = {}
candidate_percentage = {}

with open(election_data_csv, encoding='UTF-8') as election:
    
    # Specify the delimiter and the variable that holds contents.
    csvreader = csv.reader(election, delimiter=",")
    
    # Make sure the code skips the header row.
    csvheader = next(csvreader) 

    for row in csvreader:
    
    #Total number of votes cast for each person running.
        total_vote_count += 1   
        candidate = row[2]
        if candidate in candidate_list:
            candidate_votes[candidate] +=1
        else:
            candidate_votes[candidate] = 1 
            candidate_list.append(candidate)
       
    #Calculate percentage of each candidate's votes.
    percentage_of_votes = {}
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage = float(votes) / float(total_vote_count) * 100
        candidate_percentage[candidate] = percentage

    #Calculate winning vote.
    winner = max(candidate_votes, key=candidate_votes.get)

#Print Results
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {total_vote_count}")
print("-------------------------------")   
#print(f"{candidate_votes}")
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")

#Output results into a text file
results_file = os.path.join("analysis", "election_data.txt")
with open(results_file, "w") as results:

    results.write("Election Results\n")
    results.write("-------------------------------\n")
    results.write(f"Total Votes: {total_vote_count}\n")
   # results.write(f"{candidate_votes}\n")
    results.write("-------------------------------\n")
    results.write(f"Winner: {winner}\n")
    results.write("-------------------------------\n")