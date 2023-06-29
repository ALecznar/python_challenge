import csv
import os

election_data_csv = "election_data.csv"


#open csv

with open(election_data_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    
 
def election_results(data):
    total_votes = 0
    candidates = {}
    
    #loop through data
    for row in data:
        total_votes += 1
        candidate = row['Candidate']
        candidates[candidate] = candidates.get(candidate, 0) + 1
    
    result_string = "Election Results\n"
    result_string += "-------------------------\n"
    result_string += f"Total Votes: {total_votes}\n"
    result_string += "-------------------------\n"
    
    candidate_results = []
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        candidate_result = f"{candidate}: {percentage:.3f}% ({votes})"
        candidate_results.append(candidate_result)
    
    result_string += "\n".join(candidate_results) + "\n"
    result_string += "-------------------------\n"
    winner = max(candidates, key=candidates.get)
    result_string += f"Winner: {winner}\n"
    result_string += "-------------------------\n"
    
    return total_votes, result_string, winner





with open('election_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

#store the results in variables
total_votes, result_string, winner = election_results(data)

# Print the result_string
print(result_string)

# Export results to a text file
output_file = "output.txt"

with open(output_file, "w") as file:
    file.write(result_string)

