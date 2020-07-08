#Import Packages
import os
import csv

#Variables
candidates = []
candidate_pairs = []
vote_rows = []

#Establish file path and open file
poll_path = os.path.join("Resources","election_data.csv")
with open(poll_path, 'r') as csvfile:
    poll_csv = csv.reader(csvfile, delimiter=',')
    #Read header first to remove from row loop
    csv_header = next(poll_csv)
    print(csv_header)
    count = 0
    for row in poll_csv:
        if row[2] not in candidates:
            candidates.append(row[2])
        vote_rows.append(row[2])


for can_list in candidates:
    wip = 0
    sigma = 0
    for can_vote in vote_rows:
        if can_vote == can_list:
            wip += 1
        sigma += 1
    candidate_pairs.append([can_list,wip])

print(f'\nElection Results\n----------------\n'
    f'Total Votes: {sigma}\n----------------')
winner = "hold"
wip = 0
for a,b in candidate_pairs:
    if b > wip:
        wip = b
        winner = a
    print(f'{a}: {"{0:.2%}".format(float(b/sigma))} ({b})')
print('----------------\n'
    f'Winner: {winner}')

output_path = os.path.join("Analysis","output.txt")
with open(output_path, 'w') as txtfile:
    print(f'\nElection Results\n----------------\n'
        f'Total Votes: {sigma}\n----------------', file=txtfile)
    for a,b in candidate_pairs:
        print(f'{a}: {"{0:.2%}".format(float(b/sigma))} ({b})', file=txtfile)
    print('----------------\n'
        f'Winner: {winner}', file=txtfile)
