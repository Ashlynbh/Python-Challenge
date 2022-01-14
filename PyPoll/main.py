#######
#PREPARE
#######

#IMPORT LIBRARIES 
from itertools import count
from math import comb
import os 
import csv
from statistics import mean
import statistics
from collections import Counter


#DEFINING VARIABLES 
voter_id_list = []
candidate_list = []
total_votes = 0 
votes_count = 0 
winner = ""
winner_count = 0 
candidate = ""
percent_votes = []
combined_candidates = ""

#LOCATE THE DATA 
election_csv = os.path.join("Resources", "election.csv")

# OPEN AND READ DATA 
with open(election_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header = next (csv_file) 

    for row in csvreader: 
#SPLIT DATA INTO LISTS  
# VOTER ID  
        voter_id = row
        voter_id_list.append(voter_id[0]) 

# CANDIDATE 
        candidate = row
        candidate_list.append(candidate[2])

# Calculate total votes cast  
        total_votes += 1

# Gather a list of candidates who received votes 
        def unique (candidate_list):
            print (*Counter(candidate_list))
            candidate_list.append
            return (candidate)

# Gather the total votes for each candidate 
    votes_count = [[candidate, candidate_list.count(candidate)] for candidate in set(candidate_list)]
    
# Gather the percentage of votes for each candidate 
    for name, count in votes_count:
        percent_votes = (count / total_votes) * 100
        combined_candidates = combined_candidates + f"{name}: {percent_votes:.3f}% ({count})\n"
    
#Search for the winner by sorting data 
    votes_count = sorted(votes_count, key = lambda k: k[1], reverse = True)
    winner = votes_count[0][0]

    # winner = combined_candidates [0] [0]

    #unique(candidate_list)
    #print (total_votes)
    #print (votes_count)
   # print (winner)
   
   #######
#PRINT ANALYSIS
#######

output = (
        f"Election Results\n"
        f"----------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------------------\n"
        f"{combined_candidates}\n"
        f"----------------------------------\n"
        f"Winner:{winner}\n"
)
#print output to terminal 
print(output)
print(type(combined_candidates))

text_file = open("Election.txt", "w")
n = text_file.write(output)
text_file.close()

  
