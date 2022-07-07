# Election Analysis Using Python

## Project Overview
A Colorado Board of Elections employee has asked us to help complete an election audit of a recent local congressional election.

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote

## Resources
- [PyPoll_Challenge][Resources/PyPoll_Challenge.py]

## Results
The analysis of the election shows that:
- There were a total of 369,711 votes cast in the election.

- The candidates and their vote counts are as follows:
    - Charles Casper Stockham: 23.0% of the vote (85,213 votes)
    - Diana DeGette: 73.8% of the vote (272,892 votes)
    - Raymon Anthony Doane: 3.1% of the vote (11,606 votes)

- The winner of the election was:
    **Diana DeGette** who received 73.8% of the vote (272,892 votes)

![Election_Analysis_Text][Resources/election_analysis.txt]

## Summary
The script used for this analysis is able to generate a list of candidates, their vote counts, the candidate's percentage of the total vote, and the winner of the election. In addition, it provides a breakdown of votes by county. This code can be applied to different elections that have different candidates and county information provided the .CSV format remains the same as what was used here. 

This code could modified to provide additional information that might be useful to candidates, the county elections office, and the public. For example, we could provide a breakdown of the votes cast for each candidate based on the county the votes were cast in. This would allow visualization of which counties support which candidates. In addition, this script assumes that all ballot IDs are unique. As a quality control check it would be prudent to modify the script so that only unique ballots. 