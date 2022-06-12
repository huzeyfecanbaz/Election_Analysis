# Add our dependencies.
import csv
import os
from sqlite3 import Row

# Assign a variable to load a file from a path.
file_to_load=os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")

#Initialize a total vote counter
total_votes=0

#declare a new list
candidate_options=[]

#declare an empty dictionary
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count=0
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader=csv.reader(election_data)
     # Print the header row.
    headers=next(file_reader)
        
# Print each row in the CSV file.
    for row in file_reader:
        #add total vote count
        total_votes +=1

        #Print the Candidate name from each row
        candidate_name=row[2]

       #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #add it to the list of candidates
            candidate_options.append(candidate_name)

            #begin tracking that andidate's vote count.
            candidate_votes[candidate_name]=0

        #add a vote to that candidate's count.
        candidate_votes[candidate_name]+=1

#save the results to a txt file
with open ("election_analysis.txt","w") as txt_file:
        #Determine the percentage of votes for each candidate by looping through the counts
    election_results=(
            f"\nElection Results\n"
            f"---------------------------\n"
            f"Total Votes:{total_votes:,}\n"
            f"---------------------------\n"
        )
    print(election_results, end="")
    txt_file.write(election_results)

        #1. iterate through the candidate list
    for candidate_name in candidate_votes:

            #Retrieve vote count of a candidate
        votes=candidate_votes[candidate_name]

            #Calculate the percentage
        vote_percentage=float(votes)/float(total_votes)*100

    #print candidate name and percentage of votes
        #  print(f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")
        candidate_results= (f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
            #determine winning vote count and candidate
            #determine if the votes is greater than the winning count
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name
       
        winning_candidate_summary=(
            f"--------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning vote count: {winning_count}\n"
            f"Winning Percentage: {winning_percentage:.1f}\n"
            f"--------------------------\n")
    print(winning_candidate_summary)
        
            #save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
        