#import os module
import os 

#import csv
import csv

#set path for csv file 
poll_data = r"\Users\mahan\Downloads\Starter_Code_Mod3_Challenge\Starter_Code\PyPoll\Resources\election_data.csv"

# set up and define variables 
votes_counter = 0
column_index = 2
candidate_one = "Charles Casper Stockham"
sum_candidate_one = 0
per_candidate_one = 0
candidate_two = "Diana DeGette"
sum_candidate_two = 0
per_candidate_two = 0
candidate_three = "Raymon Anthony Doane"
sum_candidate_three = 0
per_candidate_three = 0
winner = 0

# Read the csv and convert it into a list of dictionaries
with open(poll_data) as election_data:
    reader = csv.reader(election_data, delimiter= ",")
    # skip the header
    header = next(reader)
    #printing the headers to make sure it's pulling from the document correctly
    print(header)

#looping through all of the rows 
    for row in reader:
#calculate the results
        #Total number of votes
        votes_counter += 1
        #Total votes for Charles Casper Stockham 
        if row[column_index] == candidate_one:
            sum_candidate_one += 1
        #Total votes for Diane DeGette
        if row[column_index] == candidate_two:
            sum_candidate_two += 1
        #Total votes for Raymon Anthony Doane
        if row[column_index] == candidate_three:
            sum_candidate_three += 1

#calculate percentage of votes for each candidate
per_candidate_one = (sum_candidate_one/votes_counter)*100
per_candidate_two = (sum_candidate_two/votes_counter)*100
per_candidate_three = (sum_candidate_three/votes_counter)*100

#format the percentages so they are easier to read
format_per_candidate_one = round(per_candidate_one,3)
format_per_candidate_two = round(per_candidate_two,3)
format_per_candidate_three = round(per_candidate_three,3)

#keeping these open to check if the code is working
print(sum_candidate_one)
print(sum_candidate_two)
print(sum_candidate_three)

print(format_per_candidate_one)
print(format_per_candidate_two)
print(format_per_candidate_three)

#determine the winner
winner = max(sum_candidate_one,sum_candidate_two,sum_candidate_three)
if winner == sum_candidate_one:
     winner = candidate_one
if winner == sum_candidate_two:
    winner = candidate_two
if winner == sum_candidate_three:
    winner = candidate_three

#printing the winner to make sure it worked
print(winner)

#print the offical data 
print("Election Results")
print("--------------------")
print(f"Total Votes:{votes_counter}")
print("--------------------")
print(f"Charles Casper Stockham: {format_per_candidate_one}% ({sum_candidate_one})")
print("--------------------")
print(f"Diane DeGette: {format_per_candidate_two}% ({sum_candidate_two})")
print("--------------------")
print(f"Raymon Anthony Doane: {format_per_candidate_three}% ({sum_candidate_three})")
print("--------------------")
print(f"Winner: {winner}")
print("--------------------")


#create a text file for the official results data
#results_file =os.path.join("PyPoll/Analysis/Elections_Results.txt")
#print the offical results data in the new text file
#with open (results_file, "w") as textfile:
filename = "ElectionResults.txt"
outfile = open(filename, 'w')
outfile.write("Election Results")
outfile.write("\n----------------------------------------")
outfile.write(f"\nTotal Votes: {votes_counter}")
outfile.write("\n----------------------------------------")
outfile.write(f"\n{candidate_one}: {format_per_candidate_one}% ({sum_candidate_one})")
outfile.write(f"\n{candidate_two}: {format_per_candidate_two}% ({sum_candidate_two})")
outfile.write(f"\n{candidate_three}: {format_per_candidate_three}% ({sum_candidate_three})")
outfile.write("\n----------------------------------------")
outfile.write(f"\nWinner: {winner} ")
outfile.write("\n----------------------------------------")

outfile.close()
