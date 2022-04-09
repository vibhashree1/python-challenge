#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Import 
import os, csv
from pathlib import Path 

file_path = Path("Downloads", "PyPoll", "election_data.csv")

# Declare Variables 
total_votes = 0 
Charles_votes = 0
Diana_votes = 0
Raymon_votes = 0


# Open csv in default read mode
with open(file_path,newline="", encoding="utf-8") as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header so we iterate through the actual values
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # We have three candidates if the name is found, count the times it appears and store in a list
        if row[2] == "Charles Casper Stockham": 
            Charles_votes +=1
        elif row[2] == "Diana DeGette":
            Diana_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            Raymon_votes +=1
        
 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Charles", "Diana", "Raymon"]
votes = [Charles_votes,Diana_votes,Raymon_votes]
dict_c_a_v = dict(zip(candidates,votes))
key = max(dict_c_a_v, key=dict_c_a_v.get)

# Print a the summary of the analysis
Charles_percent = (Charles_votes/total_votes) *100
Diana_percent = (Diana_votes/total_votes) * 100
Raymon_percent = (Raymon_votes/total_votes)* 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles: {Charles_percent:.3f}% ({Charles_votes})")
print(f"Diana: {Diana_percent:.3f}% ({Diana_votes})")
print(f"Raymon: {Raymon_percent:.3f}% ({Raymon_votes})")
print(f"Winner: {key}")
print(f"----------------------------")

# Output files
output_file = Path("Downloads", "PyPoll", "Election_Results_Summary.txt")

with open(output_file,"w") as file:

# to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles: {Charles_percent:.3f}% ({Charles_votes})")
    file.write("\n")
    file.write(f"Diana: {Diana_percent:.3f}% ({Diana_votes})")
    file.write("\n")
    file.write(f"Raymon: {Raymon_percent:.3f}% ({Raymon_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")


# In[ ]:





# In[ ]:





# In[ ]:




