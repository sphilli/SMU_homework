import csv

candidates = []
all_candidates = []
percent_list = []
data = {}
total = 0
# Read the poll data from the CSV file
#loop through file
with open('/Users/shauntelphillips/Desktop/SMU Bootcamp/Homework/SMU_homework/Python Challenge/PyPoll/Resources/election_data.csv') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if it exists
    for row in reader:
        total += 1
        all_candidates.append(row[2])

        if row[2] not in candidates:
            candidates.append(row[2])

for i in range(len(candidates)):
    count = 0
    for j in range(len(all_candidates)):
        if candidates[i] == all_candidates[j]:
            count += 1
    data[candidates[i]] = count

print("Election Results")
print("____________________________\n")
print("Total Votes: %d" % total)
print("____________________________\n")

for candidate in candidates:
    percentage = (data[candidate] / total) * 100
    percent_list.append(percentage)
    print("%s : %.3f%% (%d)" % (candidate, percentage, data[candidate]))

print("____________________________\n")
winner = candidates[percent_list.index(max(percent_list))]
print("Winner: " + winner)
print("\t____________________________\n")