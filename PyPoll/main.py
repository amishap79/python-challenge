import os
import csv

# The total number of votes cast
total_votes = 0
# A complete list of candidates who received votes
# The total number of votes each candidate won
# The percentage of votes each candidate won
candidates= {}

# Set path for file for read file
csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")


    for row in csv_reader:
        total_votes += 1

        if row[2] not in candidates.keys():
            # add each candidate to the dictionary
            candidates[row[2]] = {"cand_total_votes": 0}

        for candidate in candidates.keys():
            if candidate == row[2]:
                # add vote to listed in this row
                candidates[candidate]["cand_total_votes"] = int(candidates[row[2]]["cand_total_votes"]) + 1

    for item in candidates.keys():
        # calcuate percentage of votes received for candidate(i.e. item)
        candidates[item]["pecentage_of_votes"] = round(candidates[item]["cand_total_votes"] / total_votes * 100, 5)


max_votes = 0
winner = {}
for item2 in candidates.keys():
    if candidates[item2]["cand_total_votes"] > max_votes:
        max_votes = candidates[item2]["cand_total_votes"]
        winner = item2

print('Election Results')
print('-----------------------------')
print(f'Total Votes: {total_votes}')
print('-----------------------------')
for item2 in candidates.keys(): 
    print(f'{item2}: {candidates[item2]["pecentage_of_votes"]}% ({candidates[item2]["cand_total_votes"]})')
print('-----------------------------')
print(f'Winner: {winner}')
print('-----------------------------')


# Open the file using "write" mode. Specify the variable to hold the contents
txtfile = open("Resources/election_data_results.txt", "w+")
txtfile.write('Election Results\n')
txtfile.write('-----------------------------\n')
txtfile.write(f'Total Votes: {total_votes}\n')
txtfile.write('-----------------------------\n')
for item2 in candidates.keys(): 
    txtfile.write(f'{item2}: {candidates[item2]["pecentage_of_votes"]}% ({candidates[item2]["cand_total_votes"]})\n')
txtfile.write('-----------------------------\n')
txtfile.write(f'Winner: {winner}\n')
txtfile.write('-----------------------------\n')
