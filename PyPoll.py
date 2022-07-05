# Add our dependencies
import datetime, csv, os

# Assigned variable for election_results file path
file_to_load = 'r3_election-analysis/Resources/election_results.csv'

# Assign a variable to save the file to a path
file_to_save = os.path.join("r3_election-analysis", "election_analysis.txt")

# Initialize the vote counter
total_votes = 0

# List for candidate options
candidate_options = []

# Dictionary of candidates and their vote counts
candidate_votes = {}

#Track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

  # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Total vote counter
    for row in file_reader:
        total_votes += 1

        # Add unique names to candidate options list
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Initialize candidate vote counter to 0
            candidate_votes[candidate_name] = 0

    # Track votes for each candidate
        candidate_votes[candidate_name] += 1

# Determine the votes associated with each candidate
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f'{candidate_name}: received {vote_percentage:.1f}% ({votes:,}\n) of the vote.')


    # Determine the winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

# Print the winning candidates results to the terminal
winning_candidate_summary = (
    f'Winner: {candidate_name}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n')

print(winning_candidate_summary)

