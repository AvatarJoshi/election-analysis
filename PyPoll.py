# Approach
# 1.) Retrieve a list of all candidates
# 2.) Count the votes each candidate received
# 3.) Count the total votes cast
# 4.) Calculate the percentage of votes each candidate received.
# 5.) Determine the winner of the election

# Imports datetime class from the datetime module.
import datetime, csv, os
# Use the now() attribute on the date time class to get the present time.
now = datetime.datetime.now()

#Print the present time.
#print("The time right now is", now)

file_to_load = 'r3_election-analysis/Resources/election_results.csv'

#Open the election results and read the file
with open(file_to_load, 'r') as election_data:

    # To Do: Read and Analyze the Data Here

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the file
    #for row in file_reader:
        #print(row)


    
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("r3_election-analysis", "analysis", "election_analysis.txt")

# Open and be able to write to our txt file.
#with open(file_to_save, "w") as txt_file:


